"""Login com sessão, erro genérico e bloqueio por tentativas (L2, L3 e L5)."""

import math
import secrets
import time
from dataclasses import dataclass

from .erros import ContaBloqueada, CredenciaisInvalidas
from .senha import conferir
from .validacao import validar_email

LIMITE_TENTATIVAS = 3
TEMPO_BLOQUEIO_SEGUNDOS = 10 * 60
MENSAGEM_CREDENCIAIS_INVALIDAS = "E-mail ou senha inválidos."


@dataclass(frozen=True)
class Sessao:
    """Identifica o usuário logado (L2)."""

    usuario_id: int
    email: str
    token: str


def entrar(repositorio, email, senha, agora=None):
    """Faz o login e devolve uma Sessao.

    O parâmetro `agora` (timestamp em segundos) existe para os testes
    conseguirem simular a passagem do tempo; no uso normal fica vazio.
    """
    email = validar_email(email)
    agora = time.time() if agora is None else agora

    usuario = repositorio.buscar_por_email(email)
    if usuario is None:
        # Mesma mensagem da senha errada: não revela se o e-mail existe (L3).
        raise CredenciaisInvalidas(MENSAGEM_CREDENCIAIS_INVALIDAS)

    tentativas = usuario.tentativas_erradas
    bloqueado_ate = usuario.bloqueado_ate

    if bloqueado_ate > agora:
        minutos = math.ceil((bloqueado_ate - agora) / 60)
        raise ContaBloqueada(
            f"Conta bloqueada por excesso de tentativas. Tente de novo em {minutos} minuto(s)."
        )

    if bloqueado_ate:
        # O bloqueio anterior já venceu: a contagem recomeça do zero.
        tentativas, bloqueado_ate = 0, 0.0

    if not conferir(senha or "", usuario.senha_hash):
        tentativas += 1
        if tentativas >= LIMITE_TENTATIVAS:
            bloqueado_ate = agora + TEMPO_BLOQUEIO_SEGUNDOS
            tentativas = 0
        repositorio.atualizar_tentativas(usuario.id, tentativas, bloqueado_ate)
        raise CredenciaisInvalidas(MENSAGEM_CREDENCIAIS_INVALIDAS)

    if usuario.tentativas_erradas or usuario.bloqueado_ate:
        repositorio.atualizar_tentativas(usuario.id, 0, 0.0)

    return Sessao(usuario_id=usuario.id, email=usuario.email, token=secrets.token_urlsafe(32))
