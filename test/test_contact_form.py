from playwright.sync_api import Playwright, sync_playwright
from pom.contact_us_page import ContactPage
import pytest


@pytest.mark.regression
def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized", "--start-in-incognito"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    contact_us = ContactPage(page)

    contact_us.navigate()
    contact_us.submit_form("Alexs", "Suspiro", "alexis@yopmail.com", "9231223232", "ASS", "HAPPY")

    # ---------------------
    context.close()
    browser.close()