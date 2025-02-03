from base.base import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TopSellersPage(BasePage):
    __BUTTON = (By.CSS_SELECTOR, "button.DialogButton")
    __LAST_ELEMENT_ON_LEADERS = (By.CSS_SELECTOR, "table>tbody tr:last-child")

    TAG = 'h1'
    UNIQUE_TEXT = 'Top Sellers'

    def scroll_to_last_element(self):
        self.wait.until(EC.presence_of_element_located(self.__LAST_ELEMENT_ON_LEADERS))
        last_element_on_leaders = self.find_element(self.__LAST_ELEMENT_ON_LEADERS)
        self.action.scroll_to_element(last_element_on_leaders).perform()

    def click_button(self):
        self.wait.until(EC.element_to_be_clickable(self.__BUTTON))
        self.find_element(self.__BUTTON).click()

    def go_to_AllProductsPage(self):
        self.scroll_to_last_element()
        self.click_button()


