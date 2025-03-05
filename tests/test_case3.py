from pages.main_page import MainPage
from pages.tradingPlatform_page import TradingPlatformPage


def test_TradingPlatform():
    main_page = MainPage()
    main_page.open()
    assert main_page.is_opened() is True, "Страница не открылась"
    main_page.enter_to_TradingPlatformPage()

    tradingPlatform_page = TradingPlatformPage()
    assert tradingPlatform_page.is_opened(), "Страница не открылась"

    tradingPlatform_page.show_advanced_options()
    tradingPlatform_page.form_work()
    tradingPlatform_page.remove_some_filters()
    tradingPlatform_page.enter_to_FirstResultPage()
