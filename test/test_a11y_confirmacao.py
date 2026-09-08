from pytest_playwright_axe import Axe
from helpers import assert_sem_violacoes_graves
from pages.produto_detalhe_page import ProdutoDetalhePage
from pages.checkout_page import CheckoutPage

def test_a11y_confirmacao(logado):
    produto = ProdutoDetalhePage(logado)
    produto.acessar('p1')
    produto.adicionar_ao_carrinho('p1')
    
    checkout = CheckoutPage(logado)
    checkout.acessar()
    checkout.calcular_frete('11701-600')
    checkout.preencher_pagamento(nome='Rafael')
    checkout.finalizar_compra()
    
    resultado = Axe().run(logado)
    assert_sem_violacoes_graves(resultado)