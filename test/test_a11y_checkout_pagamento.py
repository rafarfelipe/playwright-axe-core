from pytest_playwright_axe import Axe
from helpers import assert_sem_violacoes_graves
from pages.produto_detalhe_page import ProdutoDetalhePage
from pages.checkout_page import CheckoutPage


def test_a11y_checkout_secao_pagamento(logado):
    produto = ProdutoDetalhePage(logado)
    produto.acessar('p1')
    produto.adicionar_ao_carrinho('p1')
    
    checkout = CheckoutPage(logado)
    checkout.acessar()
    resultado = Axe().run(logado,context=checkout.contexto_secao_pagamento())
    assert_sem_violacoes_graves(resultado)
