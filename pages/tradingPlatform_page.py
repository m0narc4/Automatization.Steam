from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from base.base import BasePage
from data_loader import DataLoader


class TradingPlatformPage(BasePage):
    __data = DataLoader().get_test_data('data')['test_case3']

    __ADVANCED_OPTIONS = (By.ID, "market_search_advanced_show")
    __POPUP_MENU = (By.ID, "market_advancedsearch_appselect")
    __GAME = (By.XPATH, f"//*[text()='{__data['game']}']")
    __HERO_SELECT = (By.CSS_SELECTOR, "select[name='category_570_Hero[]']")
    __IMMORTAL_RARITY_OPTION = (By.XPATH, f"//span[text()='{__data['rarity']}']")
    __SEARCH_INPUT = (By.ID, "advancedSearchBox")
    __SEARCH_BUTTON = (By.CSS_SELECTOR, ".market_advancedsearch_bottombuttons div:last-child")
    __FIRST_RESULT = (By.ID, "resultlink_0")
    __REMOVE_FILTER = (By.XPATH, f"//a[contains(text(), '{__data['search_text']}')]/span[@class='removeIcon']")


    TAG = 'span'
    UNIQUE_TEXT = 'Community Market'

    def show_advanced_options(self):
        advanced_options = self.find_element(self.__ADVANCED_OPTIONS)
        advanced_options.click()

    def select_game(self):
        popup_menu = self.find_element(self.__POPUP_MENU)
        popup_menu.click()

        game = self.find_element(self.__GAME)
        self.action.scroll_to_element(game).perform()
        game.click()

    def select_hero(self):
        hero = Select(self.find_element(self.__HERO_SELECT))
        hero.select_by_visible_text(self.__data['hero'])

    def select_rarity(self):
        immortal = self.find_element(self.__IMMORTAL_RARITY_OPTION)
        immortal.click()

    def enter_text_in_SearchInput(self):
        search_input = self.find_element(self.__SEARCH_INPUT)
        self.action.click(search_input).send_keys('golden').perform()

    def button_click(self):
        search_button = self.find_element(self.__SEARCH_BUTTON)
        search_button.click()

    def form_work(self):
        self.select_game()
        self.select_hero()
        self.select_rarity()
        self.enter_text_in_SearchInput()
        self.button_click()


    def remove_some_filters(self):
        remove_filter_button = self.find_element(self.__REMOVE_FILTER)
        remove_filter_button.click()
        self.wait.until(EC.invisibility_of_element_located(self.__REMOVE_FILTER))


    def enter_to_FirstResultPage(self):
        first_result = self.find_element(self.__FIRST_RESULT)
        first_result.click()

