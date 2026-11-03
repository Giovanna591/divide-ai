---
title: Como administrador da casa, quero criar uma casa e convidar os moradores por um link, para reunir todos que dividem as contas
labels: tipo:história,prioridade:must,pontos:5
---
## História
**Como** administrador da casa, **quero** criar uma casa e convidar os moradores por um link, **para** reunir todos que dividem as contas.

## Conversa (PO e Developers)
- Quem cria a casa vira automaticamente o administrador.
- O convite é um link que o administrador copia e envia por onde quiser (WhatsApp, por exemplo). O envio de e-mail não faz parte desta história.
- Nesta versão, cada usuário participa de uma única casa.

## Critérios de aceite
- [ ] O usuário cria uma casa informando apenas o nome; ele passa a ser o administrador.
- [ ] O administrador gera um link de convite que vale por 7 dias.
- [ ] Um usuário logado que abre um link válido entra na casa e aparece na lista de moradores.
- [ ] Um usuário sem conta que abre o link é levado ao cadastro e, depois de cadastrar, entra na casa.
- [ ] Um link vencido mostra "Convite expirado, peça um novo ao administrador".
- [ ] Um usuário que já pertence a uma casa não consegue entrar em outra; o sistema explica o motivo.

## Cenário
**Dado** que sou administrador da casa "República Central"
**Quando** gero um link de convite e outro usuário logado o abre em até 7 dias
**Então** esse usuário passa a aparecer na lista de moradores da "República Central"

## Estimativa
5 pontos (Planning Poker: 5, 5, convergiu na 1ª rodada).
