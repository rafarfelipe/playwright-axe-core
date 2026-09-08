from pytest_playwright_axe import Axe
from helpers import assert_sem_violacoes_graves
from pages.produto_detalhe_page import ProdutoDetalhePage

def test_a11y_produto_detalhe(logado):
    produto = ProdutoDetalhePage(logado)
    produto.acessar('p2')
    
    resultado = Axe().run(logado)
    assert_sem_violacoes_graves(resultado)