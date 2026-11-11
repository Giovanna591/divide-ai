import pytest

from divide_ai.cadastro import cadastrar
from divide_ai.erros import ContaBloqueada, CredenciaisInvalidas, DadosInvalidos
from divide_ai.login import entrar

EMAIL = "ana@email.com"
SENHA = "senhaSegura123"
AGORA = 1_000_000.0  # horário fixo para os testes de bloqueio


@pytest.fixture
def usuario(repositorio):
    return cadastrar(repositorio, EMAIL, SENHA)


# T2: login correto retorna sucesso
def test_t2_login_correto_retorna_sessao(repositorio, usuario):
    sessao = entrar(repositorio, EMAIL, SENHA)

    assert sessao.usuario_id == usuario.id
    assert sessao.email == EMAIL
    assert len(sessao.token) >= 32


# T3: senha errada retorna erro (sem dizer se foi o e-mail ou a senha)
def test_t3_senha_errada_retorna_erro_generico(repositorio, usuario):
    with pytest.raises(CredenciaisInvalidas) as senha_errada:
        entrar(repositorio, EMAIL, "senhaErrada")
    with pytest.raises(CredenciaisInvalidas) as email_inexistente:
        entrar(repositorio, "nao.existe@email.com", SENHA)

    assert str(senha_errada.value) == str(email_inexistente.value) == "E-mail ou senha inválidos."


# T5: quarta tentativa após 3 erros é recusada mesmo com senha certa
def test_t5_apos_3_senhas_erradas_bloqueia_mesmo_com_senha_certa(repositorio, usuario):
    for _ in range(3):
        with pytest.raises(CredenciaisInvalidas):
            entrar(repositorio, EMAIL, "senhaErrada", agora=AGORA)

    with pytest.raises(ContaBloqueada):
        entrar(repositorio, EMAIL, SENHA, agora=AGORA + 60)


def test_bloqueio_dura_10_minutos(repositorio, usuario):
    for _ in range(3):
        with pytest.raises(CredenciaisInvalidas):
            entrar(repositorio, EMAIL, "senhaErrada", agora=AGORA)

    with pytest.raises(ContaBloqueada):
        entrar(repositorio, EMAIL, SENHA, agora=AGORA + 9 * 60 + 59)

    assert entrar(repositorio, EMAIL, SENHA, agora=AGORA + 10 * 60).email == EMAIL


def test_login_certo_zera_as_tentativas(repositorio, usuario):
    for _ in range(2):
        with pytest.raises(CredenciaisInvalidas):
            entrar(repositorio, EMAIL, "senhaErrada", agora=AGORA)
    entrar(repositorio, EMAIL, SENHA, agora=AGORA)
    for _ in range(2):
        with pytest.raises(CredenciaisInvalidas):
            entrar(repositorio, EMAIL, "senhaErrada", agora=AGORA)

    assert entrar(repositorio, EMAIL, SENHA, agora=AGORA).email == EMAIL


def test_email_invalido_no_login_nao_consulta_o_banco(banco_proibido):
    with pytest.raises(DadosInvalidos):
        entrar(banco_proibido, "", SENHA)
