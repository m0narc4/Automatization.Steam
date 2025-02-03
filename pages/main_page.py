from base.base import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    __ABOUT_LINK = (By.XPATH, "//div[@id='global_header']//a[contains(text(), 'About')]")
    __NEW_AND_INTERESTING_PULLDOWN = (By.ID, "noteworthy_tab")
    __SALES_LEADERS = (By.CSS_SELECTOR, "a[href='https://store.steampowered.com/charts/topselling/?snr=1_4_4__12']")
    __COMMUNITY = (By.XPATH, "//div[@id='global_header']//a[contains(text(), 'COMMUNITY')]")
    __MARKET = (By.XPATH, "//div[@id='global_header']//a[contains(text(), 'Market')]")

    TAG = 'div'
    UNIQUE_TEXT = 'Steam'

    def enter_to_AboutPage(self):
        aboutPage_link = self.find_element(self.__ABOUT_LINK)
        aboutPage_link.click()

    def enter_to_TopSellersPage(self):
        new_and_interesting_pulldown = self.find_element(self.__NEW_AND_INTERESTING_PULLDOWN)

        self.action.move_to_element(new_and_interesting_pulldown).perform()
        self.wait.until(EC.visibility_of_element_located(self.__SALES_LEADERS))
        self.find_element(self.__SALES_LEADERS).click()

    def enter_to_TradingPlatformPage(self):
        community_menuitem = self.find_element(self.__COMMUNITY)

        self.action.move_to_element(community_menuitem).perform()
        self.wait.until(EC.visibility_of_element_located(self.__MARKET))
        self.find_element(self.__MARKET).click()

