from selene import browser, by


def test_github_desktop(desktop_browser_config):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()


def test_github_mobile(mobile_browser_config):
    browser.open("https://github.com/")
    browser.element(".Button-content").click()
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()
