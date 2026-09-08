from playwright.sync_api import Page
from pytest_playwright_axe import Axe


def test_primeiro_scan(page: Page):
    page.goto('https://dequeuniversity.com/demo/mars/')

    resultado = Axe().run(page)

    print(resultado.keys())

    for violacao in resultado['violations']:
        tags_wacg = [tag for tag in violacao['tags'] if tag.startswith('wcag')]
        print(f'\n[{violacao['impact']}] {violacao['id']}')
        print(f'WCGA: {tags_wacg if tags_wacg else 'Sem mapeamento Direto'}')
        for node in violacao['nodes']:
            seletor = node['target'][0]
            print(f'Seletor: {seletor}')
            print(f'Resumo {node['failureSummary']}')


def test_relatorio_html_json(page: Page):
    page.goto("https://dequeuniversity.com/demo/mars/")

    axe = Axe(output_directory="axe-reports")
    resultado = axe.run(
        page,
        filename="mars_scan",
        html_report_generated=True,
        json_report_generated=True,
    )

def test_login(logado):
    logado.goto('#/carrinho')
    logado.pause()