"""Acesso ao banco de dados (SQLite) dos usuários."""

import sqlite3
from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    email: str
    senha_hash: str
    tentativas_erradas: int = 0
    bloqueado_ate: float = 0.0


class RepositorioUsuarios:
    """Guarda os usuários em um arquivo SQLite.

    Use caminho=":memory:" para um banco temporário (é o que os testes fazem).
    """

    def __init__(self, caminho=":memory:"):
        self._conexao = sqlite3.connect(caminho)
        self._conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                senha_hash TEXT NOT NULL,
                tentativas_erradas INTEGER NOT NULL DEFAULT 0,
                bloqueado_ate REAL NOT NULL DEFAULT 0
            )
            """
        )
        self._conexao.commit()

    def buscar_por_email(self, email):
        linha = self._conexao.execute(
            "SELECT id, email, senha_hash, tentativas_erradas, bloqueado_ate "
            "FROM usuarios WHERE email = ?",
            (email,),
        ).fetchone()
        return Usuario(*linha) if linha else None

    def inserir(self, email, senha_hash):
        self._conexao.execute(
            "INSERT INTO usuarios (email, senha_hash) VALUES (?, ?)",
            (email, senha_hash),
        )
        self._conexao.commit()
        return self.buscar_por_email(email)

    def atualizar_tentativas(self, usuario_id, tentativas_erradas, bloqueado_ate):
        self._conexao.execute(
            "UPDATE usuarios SET tentativas_erradas = ?, bloqueado_ate = ? WHERE id = ?",
            (tentativas_erradas, bloqueado_ate, usuario_id),
        )
        self._conexao.commit()

    def fechar(self):
        self._conexao.close()
