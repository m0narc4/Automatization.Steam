from base.base import BasePage

from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    __first_game_DOM_path = "#search_resultsRows a:first-child"
    __FIRST_GAME_TITLE = (By.CSS_SELECTOR, f"{__first_game_DOM_path} span.title")
    __FIRST_GAME_RELEASE_DATE = (By.CSS_SELECTOR, f"{__first_game_DOM_path} .search_released")
    __FIRST_GAME_PRICE = (By.CSS_SELECTOR, f"{__first_game_DOM_path} .discount_final_price")


    def get_title(self):
        return self.find_element(self.__FIRST_GAME_TITLE).text

    def get_releaseDate(self):
        return self.find_element(self.__FIRST_GAME_RELEASE_DATE).text

    def get_price(self):
        return self.find_element(self.__FIRST_GAME_PRICE).text

    def go_to_FirstGamePage(self):
        self.find_element(self.__FIRST_GAME_TITLE).click()