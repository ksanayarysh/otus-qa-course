"""Testing grid """


def test_firefox(firefox_browser):
    """This happens in virtual box"""
    firefox_browser.get("http://www.lenta.ru")
    assert firefox_browser.title == "Lenta.ru - Новости России и мира сегодня"


def test_chrome(chrome_browser):
    """This happens in here"""
    chrome_browser.get("http://www.lenta.ru")
    assert chrome_browser.title == "Lenta.ru - Новости России и мира сегодня"
