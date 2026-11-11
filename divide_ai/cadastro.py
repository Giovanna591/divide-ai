"""Cadastro de usuários (L1 e L6)."""

from .erros import DadosInvalidos, EmailJaCadastrado
from .senha import gerar_hash
from .validacao import validar_email

TAMANHO_MINIMO_SENHA = 8


def cadastrar(repositorio, email, senha):
    """Cria um usuário e devolve ele já salvo no banco.

    - e-mail vazio ou sem @ é rejeitado antes de consultar o banco (L4);
    - senha com menos de 8 caracteres é rejeitada (L6);
    - a senha é gravada como hash, nunca em texto puro (L1).
    """
    email = validar_email(email)

    if senha is None or len(senha) < TAMANHO_MINIMO_SENHA:
        raise DadosInvalidos(
            f"A senha deve ter pelo menos {TAMANHO_MINIMO_SENHA} caracteres."
        )

    if repositorio.buscar_por_email(email) is not None:
        raise EmailJaCadastrado("E-mail já cadastrado.")

    return repositorio.inserir(email, gerar_hash(senha))
