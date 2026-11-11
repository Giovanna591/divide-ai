"""Linha de comando do Divide Aí.

Exemplos:
    python -m divide_ai cadastrar ana@email.com
    python -m divide_ai entrar ana@email.com

A senha é pedida no terminal, sem aparecer na tela.
O banco fica no arquivo divide_ai.db (ou no caminho da variável DIVIDE_AI_BANCO).
"""

import argparse
import getpass
import os
import sys

from .erros import ErroDivideAi
from .repositorio import RepositorioUsuarios


def executar(comando, repositorio, email, senha):
    raise ErroDivideAi(f"O comando '{comando}' ainda não foi implementado.")


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="python -m divide_ai",
        description="Divide Aí: cadastro e login de usuários.",
    )
    comandos = parser.add_subparsers(dest="comando", required=True)
    comandos.add_parser("cadastrar", help="cria uma conta").add_argument("email")
    comandos.add_parser("entrar", help="faz login").add_argument("email")
    args = parser.parse_args(argv)

    senha = getpass.getpass("Senha: ")
    repositorio = RepositorioUsuarios(os.environ.get("DIVIDE_AI_BANCO", "divide_ai.db"))
    try:
        print(executar(args.comando, repositorio, args.email, senha))
        return 0
    except ErroDivideAi as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1
    finally:
        repositorio.fechar()


if __name__ == "__main__":
    sys.exit(main())
