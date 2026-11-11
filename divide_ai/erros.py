"""Erros usados pelo módulo de contas do Divide Aí."""


class ErroDivideAi(Exception):
    """Erro base: qualquer falha esperada de cadastro ou login."""


class DadosInvalidos(ErroDivideAi):
    """E-mail ou senha não passaram na validação."""


class EmailJaCadastrado(ErroDivideAi):
    """Já existe uma conta com este e-mail."""


class CredenciaisInvalidas(ErroDivideAi):
    """E-mail ou senha incorretos (sem dizer qual dos dois)."""


class ContaBloqueada(ErroDivideAi):
    """Conta bloqueada temporariamente por excesso de senhas erradas."""
