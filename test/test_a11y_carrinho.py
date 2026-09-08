from pytest_playwright_axe import Axe
from helpers import assert_sem_violacoes_graves
from pages.carrinho_page import CarrinhoPage
from pages.produto_detalhe_page import ProdutoDetalhePage


def test_a11y_carrinho(logado):
    produto_detalhe = ProdutoDetalhePage(logado)
    produto_detalhe.acessar('p2')
    produto_detalhe.adicionar_ao_carrinho('p2')
    carrinho = CarrinhoPage(logado)
    carrinho.acessar()
    resultado = Axe().run(logado)
    assert_sem_violacoes_graves(resultado)