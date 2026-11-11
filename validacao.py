"""Validação dos dados digitados pelo usuário.

A validação acontece antes de qualquer consulta ao banco (L4).
"""

from .erros import DadosInvalidos


def validar_email(email):
    """Confere o formato do e-mail e devolve ele normalizado (sem espaços, minúsculo).

    Rejeita e-mail vazio, sem @ ou sem texto antes ou depois do @.
    """
    if email is None or not email.strip():
        raise DadosInvalidos("Informe o e-mail.")

    email = email.strip().lower()
    usuario, arroba, dominio = email.partition("@")
    if not arroba or not usuario or not dominio:
        raise DadosInvalidos("E-mail inválido.")

    return email
