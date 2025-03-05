import time
import re

from base.base import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AboutPage(BasePage):
    __ABOUT_LINK = ("xpath", "(//div[@class='supernav_container']/a)[3]")
    __PLAYING_NOW_LOCATOR = ("xpath", "//*[contains(@class,'gamers_in_game')]/..")
    __ONLINE_LOCATOR = ("xpath", "//*[contains(@class,'gamers_online')]/..")

    TAG = 'div'
    UNIQUE_TEXT = 'online'

    def get_numb(self, str):
        str = str.replace(',', '.')
        result = ''
        for char in str:
            if char.isdigit() or char == '.':
                result += char
        time.sleep(2)
        return float(re.findall(r'\d+\.\d+', str)[0])

    def get_playing_now(self):
        self.wait.until(EC.visibility_of_element_located(AboutPage.__PLAYING_NOW_LOCATOR))
        online_label = self.find_element(self.__PLAYING_NOW_LOCATOR).text
        return self.get_numb(online_label)

    def get_online(self):
        self.wait.until(EC.visibility_of_element_located(self.__ONLINE_LOCATOR))
        playing_now = self.find_element(self.__ONLINE_LOCATOR).text
        return self.get_numb(playing_now)

    def go_to_store(self):
        self.open()