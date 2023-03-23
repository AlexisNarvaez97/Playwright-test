import pytest
from playwright.sync_api import Playwright, expect
from pom.home_page_elements import HomePage


def test_about_us(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


def test_about_us_2(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://symonstorozhenko.wixsite.com/website-1")
        home_page = HomePage(page)
        expect(home_page.celebrate_header).to_be_visible()
        expect(home_page.celebrate_body).to_be_visible()

        # ---------------------
        context.close()
        browser.close()
