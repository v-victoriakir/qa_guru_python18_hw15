import pytest
from selene import browser, by


@pytest.mark.parametrize("desktop_browser_config", [(1600, 900)], indirect=True)
def test_desktop(desktop_browser_config):
    browser.open("http://github.com")
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()


@pytest.mark.parametrize("mobile_browser_config", [(430, 932)], indirect=True)
def test_mobile(mobile_browser_config):
    browser.open("https://github.com/")
    browser.element(".Button-content").click()
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()
