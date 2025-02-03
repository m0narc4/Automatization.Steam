from base.base import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AboutPage(BasePage):
    __ABOUT_LINK = ("xpath", "(//div[@class='supernav_container']/a)[3]")
    __PLAYING_NOW_LOCATOR = ("xpath", "(//div[@class='online_stat'])[1]")
    __ONLINE_LOCATOR = ("xpath", "(//div[@class='online_stat'])[2]")

    TAG = 'div'
    UNIQUE_TEXT = 'online'

    def get_online(self):
        self.wait.until(EC.visibility_of_element_located(AboutPage.__PLAYING_NOW_LOCATOR))
        online_label = self.__PLAYING_NOW_LOCATOR
        return self.find_element(online_label).text

    def get_playing_now(self):
        self.wait.until(EC.visibility_of_element_located(self.__ONLINE_LOCATOR))
        playing_now = self.__ONLINE_LOCATOR
        return self.find_element(playing_now).text

    def compare_stats(self):
        if self.get_online() > self.get_playing_now():
            return "Число игроков сейчас меньше, чем онлайн"
        return "Число игроков сейчас больше, чем онлайн"

    def go_to_store(self):
        self.open()