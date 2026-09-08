from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def acessar(self):
        self.page.goto(f'#/checkout')
        
    def contexto_secao_pagamento(self):
        seletor = '[data-testid="checkout-secao-pagamento"]'
        return f"'{seletor}'"
    
    def calcular_frete(self, cep):
        self.page.get_by_test_id('checkout-cep-input').fill(cep)
        self.page.get_by_test_id('cupom-aplicar-button').click()
        
    def preencher_pagamento(self, nome='Cliente Teste', numero='4111111111111111', validade='12/25', cvv='123'):
        self.page.get_by_test_id('checkout-pagamento-nome-cartao-input').fill(nome)
        self.page.get_by_test_id('checkout-pagamento-numero-cartao-input').fill(numero)
        self.page.get_by_test_id('checkout-pagamento-validade-input').fill(validade)
        self.page.get_by_test_id('checkout-pagamento-cvv-input').fill(cvv)
        
    def finalizar_compra(self):
        self.page.get_by_test_id('checkout-finalizar-button').click()