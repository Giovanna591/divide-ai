import pytest

from divide_ai.repositorio import RepositorioUsuarios


@pytest.fixture
def repositorio():
    """Banco SQLite em memória, novo a cada teste."""
    repo = RepositorioUsuarios(":memory:")
    yield repo
    repo.fechar()


class RepositorioQueNaoPodeSerUsado:
    """Falha o teste se alguém tentar consultar o banco."""

    def __getattr__(self, nome):
        raise AssertionError(f"O banco foi consultado ({nome}) antes da validação.")


@pytest.fixture
def banco_proibido():
    return RepositorioQueNaoPodeSerUsado()
