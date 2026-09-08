import pytest
from playwright.async_api import Page

@pytest.fixture
def logado(page : Page):
    page.goto('')
    page.locator('[data-testid="login-email-input"]').fill('cliente@shopdemo.com')
    page.locator('[data-testid="login-senha-input"]').fill('senha123')
    page.locator('[data-testid="login-submit-button"]').click()
    yield page