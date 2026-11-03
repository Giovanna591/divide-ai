---
title: Como morador, quero criar uma conta com e-mail e senha, para acessar as despesas da casa de qualquer dispositivo
labels: tipo:história,prioridade:must,pontos:3
---
## História
**Como** morador, **quero** criar uma conta com e-mail e senha, **para** acessar as despesas da casa de qualquer dispositivo.

## Conversa (PO e Developers)
- O cadastro pede nome, e-mail e senha. Não há login social nesta versão.
- O e-mail é o identificador único da conta.
- A recuperação de senha não entra aqui; se for necessária, vira outra história.

## Critérios de aceite
- [ ] O cadastro exige nome, e-mail válido e senha com pelo menos 8 caracteres.
- [ ] Não é possível cadastrar dois usuários com o mesmo e-mail; o sistema mostra a mensagem "E-mail já cadastrado".
- [ ] A senha é armazenada com hash (nunca em texto puro).
- [ ] Após o cadastro ou login, o usuário é levado à página da sua casa (ou à tela "Criar ou entrar em uma casa", se ainda não tiver uma).
- [ ] Com e-mail ou senha incorretos, o login mostra "E-mail ou senha inválidos", sem indicar qual dos dois está errado.

## Cenário
**Dado** que sou um morador sem conta
**Quando** informo nome, um e-mail ainda não cadastrado e uma senha de 8 caracteres ou mais
**Então** minha conta é criada
**E** vejo a tela "Criar ou entrar em uma casa"

## Estimativa
3 pontos (Planning Poker: 2, 3 → 3, 3).
