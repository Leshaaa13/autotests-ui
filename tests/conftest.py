import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def chromiun_page() -> Page:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()