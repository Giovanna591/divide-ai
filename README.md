# Divide Aí

> Para estudantes que dividem moradia e perdem tempo (e amizades) acertando contas da casa, o **Divide Aí** é uma aplicação web de controle de despesas compartilhadas que mostra, a qualquer momento, quem deve quanto a quem. Diferente da planilha no grupo do WhatsApp, o nosso cálculo de saldo é automático e cada despesa fica registrada com quem pagou e como foi dividida.

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

## Equipe

| Integrante | Papel no Scrum |
|---|---|
| [Nome 1] | Product Owner |
| [Nome 2] | Scrum Master e Developer |
| [Nome 3] | Developer |

> Com 3 pessoas, o Scrum Master também desenvolve. O PO participa das conversas e dos critérios de aceite, mas não estima nem decide como implementar.

## Matriz RACI

R = Responsável · A = Aprovador · C = Consultado · I = Informado

| Atividade | PO ([Nome 1]) | Scrum Master ([Nome 2]) | Developers ([Nome 2], [Nome 3]) | Professor |
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

## Product Backlog

O backlog está nas [Issues](../../issues) do repositório, ordenado no quadro **Projects**. Labels usadas:

- `tipo:história`
- `prioridade:must` · `prioridade:should` · `prioridade:could`
- `pontos:N` (story points do Planning Poker)

| # | História | Prioridade | Pontos |
|:-:|---|:-:|:-:|
| 1 | Como morador, quero criar uma conta com e-mail e senha, para acessar as despesas da casa de qualquer dispositivo | Must | 3 |
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

| História | Votos (rodada 1 → rodada 2) | Final | Justificativa |
|---|---|:-:|---|
| #1 Criar conta | 2, 3 → 3, 3 | **3** | Maior que a referência: tem validação, hash de senha e sessão. Tecnologia conhecida, poucas dúvidas. |
| #3 Registrar despesa | 3, 5 → 3, 3 | **3** | Quem votou 5 pensou na divisão desigual, que foi separada na história #7. Com divisão igual, é um formulário com gravação e lista. |
| #2 Criar casa e convidar | 5, 5 | **5** | Duas telas, link com token e validade, regra de um morador por casa. Convergiu na primeira rodada. |
| #4 Ver saldo | 5, 8 → 5, 5 | **5** | Quem votou 8 temia simplificar dívidas entre várias pessoas. Combinado: nesta história o saldo é por par de moradores; a simplificação entra depois, se necessário. |

**Total estimado no topo do backlog: 16 pontos.**

## Definition of Done

Uma história só é considerada pronta quando:

- [ ] Todos os critérios de aceite da issue estão marcados.
- [ ] O código está em um pull request revisado por pelo menos 1 outro Developer.
- [ ] Os testes automatizados passam no CI.
- [ ] Não há bugs críticos abertos relacionados à história.
- [ ] A funcionalidade foi demonstrada ao PO.

## Quadro do projeto

GitHub Projects com as colunas: **Backlog → Pronto para sprint → Em andamento → Em revisão → Concluído**.
