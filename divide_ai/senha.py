"""Hash de senha com PBKDF2-SHA256 (biblioteca padrão do Python).

A senha nunca é gravada em texto puro (L1). O valor salvo no banco tem o formato
pbkdf2_sha256$<iterações>$<salt>$<hash>.
"""

import hashlib
import hmac
import secrets

ALGORITMO = "pbkdf2_sha256"
ITERACOES = 100_000


def _calcular(senha, salt, iteracoes):
    return hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, iteracoes)


def gerar_hash(senha):
    """Gera o hash de uma senha com um salt aleatório."""
    salt = secrets.token_bytes(16)
    resultado = _calcular(senha, salt, ITERACOES)
    return f"{ALGORITMO}${ITERACOES}${salt.hex()}${resultado.hex()}"


def conferir(senha, hash_salvo):
    """Diz se a senha digitada corresponde ao hash salvo."""
    try:
        algoritmo, iteracoes, salt_hex, esperado_hex = hash_salvo.split("$")
    except ValueError:
        return False
    if algoritmo != ALGORITMO:
        return False
    calculado = _calcular(senha, bytes.fromhex(salt_hex), int(iteracoes))
    return hmac.compare_digest(calculado.hex(), esperado_hex)
