---
title: Como morador, quero ver quanto devo e quanto tenho a receber de cada pessoa, para saber como acertar as contas
labels: tipo:história,prioridade:must,pontos:5
---
## História
**Como** morador, **quero** ver quanto devo e quanto tenho a receber de cada pessoa, **para** saber como acertar as contas.

## Conversa (PO e Developers)
- O saldo é calculado por par de moradores: entre Ana e Bruno, as dívidas nos dois sentidos se compensam.
- A simplificação de dívidas em cadeia (A deve a B, B deve a C, então A paga direto a C) não entra nesta história.
- Os pagamentos entre moradores entram na história #5. Até lá, o saldo considera só as despesas.

## Critérios de aceite
- [ ] A página "Saldo" mostra, para cada outro morador, uma linha com "Você deve R$ X a Fulano", "Fulano te deve R$ X" ou "Vocês estão quites".
- [ ] No topo aparece o saldo total do usuário: total a receber menos total a pagar.
- [ ] Dívidas nos dois sentidos entre o mesmo par se compensam e só a diferença é exibida.
- [ ] O saldo é atualizado assim que uma despesa é registrada, sem precisar recarregar a página manualmente.
- [ ] A soma dos saldos totais de todos os moradores é sempre R$ 0,00 (teste automatizado).

## Cenário
**Dado** que Ana pagou "Luz" de R$ 90,00 dividida entre Ana, Bruno e Carla
**E** que Bruno pagou "Mercado" de R$ 60,00 dividida entre Ana e Bruno
**Quando** Ana abre a página "Saldo"
**Então** ela vê "Vocês estão quites" na linha de Bruno (R$ 30,00 que ele deve menos R$ 30,00 que ela deve)
**E** "Carla te deve R$ 30,00"
**E** seu saldo total é + R$ 30,00

## Estimativa
5 pontos (Planning Poker: 5, 8 → 5, 5). Quem votou 8 temia a simplificação em cadeia; a equipe combinou deixá-la fora desta história.
