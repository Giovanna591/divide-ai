#!/usr/bin/env bash
# Cria no GitHub: labels, issues do backlog e o quadro Projects com as colunas da disciplina.
#
# Pré-requisitos:
#   1. GitHub CLI instalado (https://cli.github.com) e logado:  gh auth login
#   2. Permissão para Projects:                                gh auth refresh -s project
#   3. Repositório já criado e com o README.md enviado.
#
# Uso (rodar dentro da pasta divide-ai):
#   ./setup-github.sh DONO/REPOSITORIO            # cria tudo
#   ./setup-github.sh DONO/REPOSITORIO --dry-run  # só mostra o que faria

set -euo pipefail

REPO="${1:-}"
DRY_RUN="${2:-}"
if [[ -z "$REPO" || "$REPO" != */* ]]; then
  echo "Uso: $0 DONO/REPOSITORIO [--dry-run]" >&2
  exit 1
fi
OWNER="${REPO%%/*}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ISSUES_DIR="$SCRIPT_DIR/issues"
PROJECT_TITLE="Divide Aí - Backlog"

run() {
  if [[ "$DRY_RUN" == "--dry-run" ]]; then
    echo "[dry-run] $*"
  else
    "$@"
  fi
}

# ---------- 1. Labels ----------
echo "==> Criando labels"
create_label() { run gh label create "$1" --repo "$REPO" --color "$2" --description "$3" --force; }
create_label "tipo:história"      "1D76DB" "História de usuário"
create_label "prioridade:must"    "B60205" "MoSCoW: sem isso o produto não existe"
create_label "prioridade:should"  "D93F0B" "MoSCoW: importante, mas há contorno"
create_label "prioridade:could"   "FBCA04" "MoSCoW: desejável se houver tempo"
for p in 1 2 3 5 8 13; do
  create_label "pontos:$p" "C5DEF5" "Estimativa em story points"
done

# ---------- 2. Quadro Projects ----------
echo "==> Criando o quadro Projects"
if [[ "$DRY_RUN" == "--dry-run" ]]; then
  PROJECT_NUMBER="N"
  run gh project create --owner "$OWNER" --title "$PROJECT_TITLE"
else
  PROJECT_NUMBER=$(gh project create --owner "$OWNER" --title "$PROJECT_TITLE" --format json --jq '.number')
  gh project link "$PROJECT_NUMBER" --owner "$OWNER" --repo "$REPO" || true
  PROJECT_ID=$(gh project view "$PROJECT_NUMBER" --owner "$OWNER" --format json --jq '.id')
  STATUS_FIELD_ID=$(gh project field-list "$PROJECT_NUMBER" --owner "$OWNER" --format json \
    --jq '.fields[] | select(.name=="Status") | .id')

  # Troca as opções padrão (Todo / In Progress / Done) pelas colunas combinadas.
  gh api graphql -f query='
    mutation($field: ID!) {
      updateProjectV2Field(input: {
        fieldId: $field
        singleSelectOptions: [
          {name: "Backlog",            color: GRAY,   description: "Itens ordenados pelo PO"}
          {name: "Pronto para sprint", color: BLUE,   description: "Refinado, com critérios de aceite e pontos"}
          {name: "Em andamento",       color: YELLOW, description: "Sendo implementado"}
          {name: "Em revisão",         color: PURPLE, description: "Pull request aberto"}
          {name: "Concluído",          color: GREEN,  description: "Atende à Definition of Done"}
        ]
      }) { projectV2Field { ... on ProjectV2SingleSelectField { id } } }
    }' -f field="$STATUS_FIELD_ID" > /dev/null \
  || echo "AVISO: não consegui renomear as colunas. Ajuste manualmente no quadro (Settings > Status)."

  BACKLOG_OPTION_ID=$(gh project field-list "$PROJECT_NUMBER" --owner "$OWNER" --format json \
    --jq '.fields[] | select(.name=="Status") | .options[] | select(.name=="Backlog") | .id' || true)
fi

# ---------- 3. Issues (na ordem do backlog) ----------
echo "==> Criando issues"
for file in "$ISSUES_DIR"/*.md; do
  title=$(awk '/^---$/{n++; next} n==1 && /^title:/{sub(/^title: */, ""); print; exit}' "$file")
  labels=$(awk '/^---$/{n++; next} n==1 && /^labels:/{sub(/^labels: */, ""); print; exit}' "$file")
  body=$(awk '/^---$/{n++; next} n>=2' "$file")

  echo "  - $title"
  if [[ "$DRY_RUN" == "--dry-run" ]]; then
    run gh issue create --repo "$REPO" --title "$title" --label "$labels" --body "<conteúdo de $(basename "$file")>"
    run gh project item-add "$PROJECT_NUMBER" --owner "$OWNER" --url "<url da issue>"
    continue
  fi

  url=$(gh issue create --repo "$REPO" --title "$title" --label "$labels" --body "$body")
  item_id=$(gh project item-add "$PROJECT_NUMBER" --owner "$OWNER" --url "$url" --format json --jq '.id')
  if [[ -n "${BACKLOG_OPTION_ID:-}" ]]; then
    gh project item-edit --id "$item_id" --project-id "$PROJECT_ID" \
      --field-id "$STATUS_FIELD_ID" --single-select-option-id "$BACKLOG_OPTION_ID" > /dev/null
  fi
done

echo
echo "Pronto! Confira:"
echo "  Issues:  https://github.com/$REPO/issues"
echo "  Quadro:  https://github.com/$OWNER?tab=projects  (\"$PROJECT_TITLE\")"
echo "Lembrete: adicione o professor como colaborador (se o repositório for privado) e envie o link no Teams."
