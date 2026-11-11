import pytest

from divide_ai.erros import DadosInvalidos
from divide_ai.validacao import validar_email


# T4: e-mail inválido é rejeitado
@pytest.mark.parametrize("email", ["", "   ", None, "giovanna.email.com", "@email.com", "ana@"])
def test_t4_email_invalido_e_rejeitado(email):
    with pytest.raises(DadosInvalidos):
        validar_email(email)


def test_email_valido_volta_normalizado():
    assert validar_email("  Ana@Email.COM ") == "ana@email.com"
