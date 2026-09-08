from pytest_playwright_axe import Axe
from helpers import assert_sem_violacoes_graves
from pages.catalago_page import CatalogoPage


def test_a11y_catalogo(logado):
    catalogo = CatalogoPage(logado)
    catalogo.acessar()
    resultado = Axe().run(logado)
    assert_sem_violacoes_graves(resultado)