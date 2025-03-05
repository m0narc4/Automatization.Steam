import time

from pages.main_page import MainPage
from pages.about_page import AboutPage


def test_AboutPage():
    main_page = MainPage()
    main_page.open()
    assert main_page.is_opened() is True, "Страница не открылась"
    main_page.enter_to_AboutPage()

    about_page = AboutPage()
    assert about_page.is_opened() is True, "Страница не открылась"

    v1 = about_page.get_playing_now()
    v2 = about_page.get_online()
    assert v1 < v2, 'Число игроков сейчас меньше, чем онлайн'

    about_page.go_to_store()
    assert main_page.is_opened() is True, "Страница не открылась"
