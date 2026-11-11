import pytest

from divide_ai.cadastro import cadastrar
from divide_ai.erros import DadosInvalidos, EmailJaCadastrado
from divide_ai.senha import conferir


# T1: cadastro válido grava senha diferente da digitada
def test_t1_cadastro_valido_grava_hash_e_nao_a_senha(repositorio):
    cadastrar(repositorio, "ana@email.com", "senhaSegura123")

    salvo = repositorio.buscar_por_email("ana@email.com")
    assert salvo is not None
    assert salvo.senha_hash != "senhaSegura123"
    assert "senhaSegura123" not in salvo.senha_hash
    assert conferir("senhaSegura123", salvo.senha_hash)


# T6: senha curta é rejeitada
def test_t6_senha_com_menos_de_8_caracteres_e_rejeitada(repositorio):
    with pytest.raises(DadosInvalidos):
        cadastrar(repositorio, "ana@email.com", "1234567")

    assert repositorio.buscar_por_email("ana@email.com") is None


def test_senha_com_exatamente_8_caracteres_e_aceita(repositorio):
    assert cadastrar(repositorio, "ana@email.com", "12345678").email == "ana@email.com"


def test_email_repetido_e_rejeitado(repositorio):
    cadastrar(repositorio, "ana@email.com", "senhaSegura123")
    with pytest.raises(EmailJaCadastrado):
        cadastrar(repositorio, "ANA@email.com", "outraSenha123")


def test_email_invalido_no_cadastro_nao_consulta_o_banco(banco_proibido):
    with pytest.raises(DadosInvalidos):
        cadastrar(banco_proibido, "sem-arroba", "senhaSegura123")
