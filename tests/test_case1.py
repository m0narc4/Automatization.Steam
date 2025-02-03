from pages.main_page import MainPage
from pages.about_page import AboutPage


def test():
    main_page = MainPage()
    main_page.open()
    assert main_page.is_opened() is True, "Страница не открылась"
    main_page.enter_to_AboutPage()

    about_page = AboutPage()
    assert about_page.is_opened() is True, "Страница не открылась"
    about_page.go_to_store()