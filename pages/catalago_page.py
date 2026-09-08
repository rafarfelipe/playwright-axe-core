from playwright.sync_api import Page


class CatalogoPage:
    def __init__(self, page: Page):
        self.page = page

    def acessar(self):
        self.page.goto('#/')