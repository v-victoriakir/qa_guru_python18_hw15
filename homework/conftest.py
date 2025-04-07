import pytest
from selene import browser


def show_screen_size(screen_size):
    return f"screen size: {screen_size[0]}x{screen_size[1]}"


@pytest.fixture(params=[(1280, 720)], ids=show_screen_size)
def desktop_browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(1010, 1300)], ids=show_screen_size)
def mobile_browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(1280, 720), (1010, 1300)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1010:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()
