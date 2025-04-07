import pytest
from selene import browser, by


def test_mobile_skip(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Пропуск, т.к. это мобильное разрешение")
    browser.open("http://github.com")
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()


def test_desktop_skip(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Пропуск, т.к. это десктопное разрешение")
    browser.open("https://github.com/")
    browser.element(".Button-content").click()
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()
