# Divide Aí

## O que é

O Divide Aí é uma aplicação para quem divide moradia (repúblicas, apartamentos) controlar as despesas da casa e saber quem deve quanto a quem.

Nesta primeira sprint a equipe entregou o **login**: cadastro com senha protegida por hash, login com sessão, mensagem de erro genérica, validação de e-mail e bloqueio da conta por 10 minutos após 3 senhas erradas. Ele roda pela linha de comando e está escrito em Python.

> Para estudantes que dividem moradia e perdem tempo (e amizades) acertando contas da casa, o **Divide Aí** é uma aplicação web de controle de despesas compartilhadas que mostra, a qualquer momento, quem deve quanto a quem. Diferente da planilha no grupo do WhatsApp, o nosso cálculo de saldo é automático e cada despesa fica registrada com quem pagou e como foi dividida.

## Equipe

| Integrante | GitHub | Papel |
|---|---|---|
| Giovanna Hototian | [@Giovanna591](https://github.com/Giovanna591) | Product Owner (PO) |
| Julya Dias | [@Julyxdias](https://github.com/Julyxdias) | Scrum Master (SM) e Developer |
| Karolaine Helena | [@Karolaine231](https://github.com/Karolaine231) | Developer |

Na Sprint 1 todas implementaram uma parte do login, cada uma na sua branch e com o seu pull request.

## Como rodar o projeto

Precisa do **Python 3.10 ou mais novo**. No Windows, troque `python` por `py` se o comando não for encontrado.

```bash
git clone https://github.com/Giovanna591/divide-ai.git
cd divide-ai
pip install -r requirements.txt
```

Criar uma conta e fazer login (a senha é pedida no terminal e não aparece enquanto você digita):

```bash
python -m divide_ai cadastrar ana@email.com
python -m divide_ai entrar ana@email.com
```

Os usuários ficam no arquivo `divide_ai.db`, criado na pasta onde o comando foi executado. Para usar outro arquivo, defina a variável de ambiente `DIVIDE_AI_BANCO`.

| Situação | O que acontece |
|---|---|
| E-mail vazio ou sem @ | `Erro: E-mail inválido.` (antes de consultar o banco) |
| Senha com menos de 8 caracteres no cadastro | `Erro: A senha deve ter pelo menos 8 caracteres.` |
| E-mail ou senha errados no login | `Erro: E-mail ou senha inválidos.` |
| 4ª tentativa depois de 3 senhas erradas seguidas | `Erro: Conta bloqueada...` por 10 minutos, mesmo com a senha certa |

## Como rodar os testes

Na pasta do projeto, com um único comando:

```bash
pytest
```

Se o comando `pytest` não for encontrado, use `python -m pytest`.

| Teste | Comportamento | Arquivo |
|---|---|---|
| T1 | Cadastro válido grava senha diferente da digitada (hash) | `tests/test_cadastro.py` |
| T2 | Login correto retorna sucesso (sessão com token) | `tests/test_login.py` |
| T3 | Senha errada retorna erro genérico | `tests/test_login.py` |
| T4 | E-mail inválido é rejeitado | `tests/test_validacao.py` |
| T5 | 4ª tentativa após 3 erros é recusada mesmo com senha certa | `tests/test_login.py` |
| T6 | Senha curta é rejeitada no cadastro | `tests/test_cadastro.py` |

## Estrutura

```
divide_ai/
  __main__.py     linha de comando (cadastrar, entrar)
  cadastro.py     cadastro e senha mínima (L1, L6)
  login.py        login, erro genérico e bloqueio (L2, L3, L5)
  validacao.py    validação de e-mail (L4)
  senha.py        hash da senha (PBKDF2-SHA256)
  repositorio.py  banco SQLite dos usuários
  erros.py        erros do módulo
tests/            testes automatizados (pytest)
```

## Problema

Em repúblicas e apartamentos divididos, as contas da casa (aluguel, luz, internet, mercado, gás) são pagas por pessoas diferentes em momentos diferentes. O controle costuma ficar em mensagens soltas ou numa planilha que só uma pessoa atualiza. No fim do mês ninguém sabe ao certo quanto deve, surgem cobranças duplicadas ou esquecidas, e o acerto vira discussão.

## Público

| Papel | Quem é |
|---|---|
| **Morador** | Pessoa que divide a moradia, lança despesas que pagou e consulta o próprio saldo. |
| **Administrador da casa** | Morador que cria a casa no sistema, convida os demais e cadastra as despesas fixas. |

## Proposta de valor

Cada morador sabe, em segundos e sem fazer conta, quanto deve e quanto tem a receber.

## Funcionalidades essenciais (Must)

1. Criar conta e entrar no sistema.
2. Criar uma casa e convidar os moradores.
3. Registrar despesas informando quem pagou, com divisão igual entre os moradores.
4. Ver o saldo de cada morador: quanto deve e quanto tem a receber de cada pessoa.

## Fora de escopo (Won't, neste semestre)

- Pagamento dentro do app ou integração com Pix e bancos.
- Aplicativo nativo para Android/iOS (a aplicação web será responsiva).
- Múltiplas moedas.
- Leitura automática de comprovantes (OCR).
- Mais de uma casa por usuário.

## Como saber que funcionou

1. **Uso real:** uma casa com pelo menos 3 moradores usa o Divide Aí por 2 semanas seguidas e lança pelo menos 10 despesas.
2. **Confiabilidade do saldo:** em um conjunto de 20 despesas de teste, o saldo calculado pelo sistema bate 100% com o cálculo manual.

## Matriz RACI

Com 3 pessoas, a Scrum Master também desenvolve. Nas atividades de produto, a PO não estima nem decide como implementar.

R = Responsável · A = Aprovador · C = Consultado · I = Informado

| Atividade | PO (Giovanna) | Scrum Master (Julya) | Developers (Julya, Karolaine) | Professor |
|---|:-:|:-:|:-:|:-:|
| Definir visão e objetivo do produto | A/R | C | C | I |
| Escrever e ordenar o Product Backlog | A/R | C | C | I |
| Escrever critérios de aceite | A | I | R | I |
| Estimar itens (Planning Poker) | C | R (facilita) | A/R | I |
| Definir o escopo da sprint | C | C | A/R | I |
| Implementar e testar | I | I | A/R | I |
| Revisar pull requests | I | I | A/R | C |
| Aceitar o incremento na Review | A | I | R | C |
| Facilitar eventos e remover impedimentos | I | A/R | C | I |
| Manter o quadro Projects atualizado | C | A | R | I |
| Avaliar a entrega (nota A2/A3) | I | I | I | A/R |

Cada linha tem exatamente um A.

## Sprint 1: login

**Objetivo:** entregar o login do Divide Aí funcionando, com cadastro, entrada, erro genérico, validação de e-mail e bloqueio, e os 6 testes automatizados passando com `pytest`.

**Capacidade:** 15 pontos (3 pessoas, 2 encontros). Planejado: 13 pontos.

| Issue | História | Comportamento | Responsável | Pontos |
|:-:|---|:-:|---|:-:|
| #12 | Estrutura do projeto e README | – | @Karolaine231 | 2 |
| #13 | Validação de e-mail | L4 | @Karolaine231 | 1 |
| #14 | Cadastro com senha protegida | L1 | @Giovanna591 | 3 |
| #15 | Senha mínima de 8 caracteres | L6 | @Giovanna591 | 1 |
| #16 | Login com sucesso | L2 | @Julyxdias | 2 |
| #17 | Erro genérico na senha errada | L3 | @Julyxdias | 1 |
| #18 | Bloqueio após 3 senhas erradas | L5 | @Julyxdias | 3 |

O objetivo da sprint também está na issue fixada **#19 Sprint 1: objetivo**.

## Product Backlog

O backlog está nas [Issues](../../issues) do repositório, ordenado no quadro **Projects**. Labels usadas:

- `tipo:história`
- `prioridade:must` · `prioridade:should` · `prioridade:could`
- `pontos:N` (story points do Planning Poker)

| # | História | Prioridade | Pontos |
|:-:|---|:-:|:-:|
| 1 | Como morador, quero criar uma conta com e-mail e senha, para acessar as despesas da casa de qualquer dispositivo (dividida nas histórias #12 a #18 da Sprint 1) | Must | 3 |
| 2 | Como administrador da casa, quero criar uma casa e convidar os moradores por um link, para reunir todos que dividem as contas | Must | 5 |
| 3 | Como morador, quero registrar uma despesa informando valor, descrição, data e quem pagou, para que ela seja dividida igualmente entre os moradores | Must | 3 |
| 4 | Como morador, quero ver quanto devo e quanto tenho a receber de cada pessoa, para saber como acertar as contas | Must | 5 |
| 5 | Como morador, quero registrar que paguei a outro morador, para que a dívida seja abatida do saldo | Should | – |
| 6 | Como morador, quero editar ou excluir uma despesa que lancei, para corrigir erros de digitação | Should | – |
| 7 | Como morador, quero dividir uma despesa por valores ou porcentagens diferentes, para refletir contas em que nem todos consomem igual | Should | – |
| 8 | Como administrador da casa, quero cadastrar despesas recorrentes como aluguel e internet, para não precisar lançá-las todo mês | Should | – |
| 9 | Como morador, quero filtrar o histórico de despesas por mês e categoria, para entender onde a casa mais gasta | Could | – |
| 10 | Como morador, quero receber um e-mail quando uma nova despesa me envolver, para não ser surpreendido no fim do mês | Could | – |
| 11 | Como morador, quero anexar a foto do comprovante a uma despesa, para que os outros possam conferir o valor | Could | – |

### Registro do Planning Poker

Usamos o baralho de Fibonacci modificado (1, 2, 3, 5, 8, 13, 20, 40, 100, ?). Só os Developers votam; o PO explica e responde dúvidas.

**Referência pequena (2 pontos):** uma tela simples de listagem, sem regra de negócio (ex.: listar os moradores da casa).

| História | Votos Julya, Karolaine (rodada 1 → rodada 2) | Final | Justificativa |
|---|---|:-:|---|
| #1 Criar conta | 2, 3 → 3, 3 | **3** | Maior que a referência: tem validação, hash de senha e sessão. Tecnologia conhecida, poucas dúvidas. |
| #3 Registrar despesa | 3, 5 → 3, 3 | **3** | Quem votou 5 pensou na divisão desigual, que foi separada na história #7. Com divisão igual, é um formulário com gravação e lista. |
| #2 Criar casa e convidar | 5, 5 | **5** | Duas telas, link com token e validade, regra de um morador por casa. Convergiu na primeira rodada. |
| #4 Ver saldo | 5, 8 → 5, 5 | **5** | Quem votou 8 temia simplificar dívidas entre várias pessoas. Combinado: nesta história o saldo é por par de moradores; a simplificação entra depois, se necessário. |

**Total estimado no topo do backlog: 16 pontos.**

## Definition of Done

Uma história só é considerada pronta quando:

- [ ] Todos os critérios de aceite da issue estão marcados.
- [ ] O código está em um pull request aprovado por pelo menos 1 colega antes do merge na `main`.
- [ ] Todos os testes automatizados passam com `pytest`.
- [ ] Não há bugs críticos abertos relacionados à história.
- [ ] A funcionalidade foi demonstrada ao PO.

## Quadro do projeto

GitHub Projects (template Kanban) vinculado a este repositório, com as colunas **Backlog → Ready → In progress → In review → Done**, limite de WIP em In progress e In review e o campo **Sprint** (Iteration). As histórias da sprint vão para Done automaticamente quando o pull request que as fecha é mergeado.

## Fluxo de trabalho

1. Cada história da sprint tem uma responsável (Assignee) e uma branch criada a partir da issue (Development > Create a branch).
2. Os commits seguem o padrão `tipo: o que fez (#N)`, por exemplo `feat: valida e-mail antes de consultar o banco (#13)`.
3. O pull request tem `Closes #N`, as seções "O que foi feito" e "Como testar" e uma revisora marcada.
4. A `main` é protegida: só recebe código por pull request com 1 aprovação.
