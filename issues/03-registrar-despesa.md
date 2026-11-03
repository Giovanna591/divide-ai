---
title: Como morador, quero registrar uma despesa informando valor, descrição, data e quem pagou, para que ela seja dividida igualmente entre os moradores
labels: tipo:história,prioridade:must,pontos:3
---
## História
**Como** morador, **quero** registrar uma despesa informando valor, descrição, data e quem pagou, **para** que ela seja dividida igualmente entre os moradores.

## Conversa (PO e Developers)
- Nesta história, a divisão é sempre igual entre os moradores marcados. A divisão desigual está na história #7.
- Por padrão todos os moradores vêm marcados, mas é possível desmarcar alguém (ex.: quem não estava em casa no mês).
- Quando a divisão não for exata, os centavos que sobram ficam com quem pagou.

## Critérios de aceite
- [ ] O formulário exige descrição, valor maior que zero, data e quem pagou (por padrão, o próprio usuário).
- [ ] Todos os moradores vêm marcados para participar da divisão, e é possível desmarcar qualquer um, desde que pelo menos 1 continue marcado.
- [ ] O valor de cada participante é o valor total dividido pelo número de participantes, arredondado para baixo em centavos; a diferença fica com quem pagou.
- [ ] A despesa aparece no topo do histórico da casa, com data, descrição, valor, quem pagou e quanto coube a cada um.
- [ ] Valores negativos, zerados ou com mais de 2 casas decimais são recusados com mensagem de erro.

## Cenário
**Dado** que a casa tem 3 moradores: Ana, Bruno e Carla
**Quando** Ana registra "Conta de luz" de R$ 100,00 paga por ela, com todos marcados
**Então** a despesa aparece no histórico
**E** a parte de Bruno é R$ 33,33, a de Carla é R$ 33,33 e a de Ana é R$ 33,34

## Estimativa
3 pontos (Planning Poker: 3, 5 → 3, 3). Quem votou 5 considerou a divisão desigual, que foi separada na história #7.
