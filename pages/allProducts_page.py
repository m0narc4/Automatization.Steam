from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base import BasePage
from data_loader import DataLoader


class AllProductsPage(BasePage):
    __SEARCH_RESULT_TABLE = (By.ID, "search_result_container")

    __OS_SIDEBAR_FILTER = (By.CSS_SELECTOR, "[data-collapse-name='os']")
    __LINUX_CHECKBOX = (By.CSS_SELECTOR, "span[data-value='linux']")

    __GAMERS_COUNT_FILTER = (By.CSS_SELECTOR, "[data-collapse-name='category3']")
    __LAST = (By.CSS_SELECTOR, "[data-collapse-name='category3'] > div:last-child")
    __LAN_CHECKBOX = (By.CSS_SELECTOR, "span[data-value='48']")

    __TAGS_FILTER = (By.CSS_SELECTOR, "[data-collapse-name='tags']")
    __ACTION_GENRE_CHECKBOX = (By.CSS_SELECTOR, "span[data-value='19']")


    __GAMES_COUNT = (By.CSS_SELECTOR, "div.search_results_count")
    __REAL_GAMES_COUNT = (By.XPATH, "//div[@id='search_resultsRows']/a")

    __first_game_DOM_path = "#search_resultsRows a:first-child"
    __FIRST_GAME_TITLE = (By.CSS_SELECTOR, f"{__first_game_DOM_path} span.title")
    __FIRST_GAME_RELEASE_DATE = (By.CSS_SELECTOR, f"{__first_game_DOM_path} .search_released")
    __FIRST_GAME_PRICE = (By.CSS_SELECTOR, f"{__first_game_DOM_path} .discount_final_price")

    __data = DataLoader().get_test_data('data')['test_case2']

    TAG = 'div'
    UNIQUE_TEXT = 'All Products'

    def __make_sidebar_xpath(self, sidebar_str):
        return (By.XPATH, f"//div[contains(@class,'block search_collapse_block')]//div[contains(text(), '{sidebar_str}')]/../..")

    def __make_checkbox_xpath(self, checkbox_str):
        return (By.XPATH, f"//span[contains(@data-loc,'{checkbox_str}')]")

    def __open_collapsed(self):
        for key in self.__data.keys():
            sidebar_xpath = self.__make_sidebar_xpath(key)
            sidebar = self.find_element(sidebar_xpath)

            self.action.scroll_to_element(sidebar).perform()
            if 'collapsed' in sidebar.get_attribute('class'):
                sidebar.click()

    def __wait_until_refreshed(self):
        self.wait.until(EC.text_to_be_present_in_element_attribute(self.__SEARCH_RESULT_TABLE, 'style', 'opacity'))
        self.wait.until_not(EC.text_to_be_present_in_element_attribute(self.__SEARCH_RESULT_TABLE, 'style', 'opacity'))

    def choose_checkboxes(self):
        result = ""
        self.__open_collapsed()
        for value in self.__data.values():
            checkbox_xpath = self.__make_checkbox_xpath(value)
            checkbox = self.find_element(checkbox_xpath)

            self.action.move_to_element(checkbox).perform()
            self.wait.until(EC.element_to_be_clickable(checkbox))
            checkbox.click()
            self.__wait_until_refreshed()

            result = (result + 'True') if 'checked' in checkbox.get_attribute('class') else False
        return result

    def get_game_title(self):
        title = self.find_element(self.__FIRST_GAME_TITLE).text
        return title

    def get_game_release_date(self):
        release = self.find_element(self.__FIRST_GAME_RELEASE_DATE).text
        return release

    def get_game_price(self):
        price = self.find_element(self.__FIRST_GAME_PRICE).text
        price = price + '.'
        return price

    def get_games_count(self):
        games_count = self.find_element(self.__GAMES_COUNT).text
        for word in games_count.split(' '):
            if word.isdigit():
                return int(word)

    def get_real_games_count(self):
        real_games_count = len(self.find_elements(self.__REAL_GAMES_COUNT))
        return real_games_count

    def go_to_firstGame_page(self):
        first_game_link = self.find_element(self.__FIRST_GAME_TITLE)
        self.action.scroll_to_element(first_game_link)
        first_game_link.click()



