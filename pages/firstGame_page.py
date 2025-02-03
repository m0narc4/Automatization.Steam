from base.base import BasePage

from selenium.webdriver.common.by import By


class FirstGamePage(BasePage):
    __GAME_TITLE = (By.ID, "appHubAppName")
    __RELEASE_DATE = (By.CSS_SELECTOR, "div.release_date div.date")
    __PRICE = (By.XPATH, "//div[@class='game_purchase_price price']")

    TAG = 'h1'
    UNIQUE_TEXT = 'Buy'

    def get_game_title(self):
        title = self.find_element(self.__GAME_TITLE).text
        return title

    def get_game_release_date(self):
        release = self.find_element(self.__RELEASE_DATE).text
        return release

    def get_game_price(self):
        price = self.find_element(self.__PRICE).text
        for word in price.split(" "):
            if word.isdigit():
                return price
