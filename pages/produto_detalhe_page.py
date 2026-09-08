from playwright.sync_api import Page

class ProdutoDetalhePage:
    def __init__(self, page: Page):
        self.page = page
        
    def acessar(self, produto_id):
        self.page.goto(f'#/produto/{produto_id}')
        
    def adicionar_ao_carrinho(self, produto_id):
        self.page.get_by_test_id(f'produto-detalhe-{produto_id}-adicionar-button').click()