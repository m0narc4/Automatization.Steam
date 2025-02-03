from pages.main_page import MainPage
from pages.topsellers_page import TopSellersPage
from pages.allProducts_page import AllProductsPage
from pages.firstGame_page import FirstGamePage


def test():
    main_page = MainPage()
    main_page.open()
    assert main_page.is_opened() is True, "Страница не открылась"
    main_page.enter_to_TopSellersPage()

    topsellers_page = TopSellersPage()
    assert topsellers_page.is_opened() is True, "Страница не открылась"
    topsellers_page.go_to_AllProductsPage()

    allProducts_page = AllProductsPage()
    assert allProducts_page.is_opened() is True, "Страница не открылась"
    assert allProducts_page.choose_checkboxes() == 'TrueTrueTrue', 'Один из чекбоксов не выбран'
    title1 = allProducts_page.get_game_title()
    release1 = allProducts_page.get_game_release_date()
    price1 = allProducts_page.get_game_price()
    assert allProducts_page.get_games_count() == allProducts_page.get_real_games_count(), 'Количество результатов поиска не соответствует реальному количеству'
    allProducts_page.go_to_firstGame_page()

    firstGame_page = FirstGamePage()
    assert firstGame_page.is_opened() is True, "Страница не открылась"
    title2 = firstGame_page.get_game_title()
    release2 = firstGame_page.get_game_release_date()
    price2 = firstGame_page.get_game_price()

    assert title1 == title2 and release1 == release2 and price1 == price2, "Данные не совпадают"


