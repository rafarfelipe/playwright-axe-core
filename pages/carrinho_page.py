from playwright.sync_api import Page


class CarrinhoPage:
    def __init__(self, page: Page):
        self.page = page

    def acessar(self):
        self.page.goto('#/carrinho')