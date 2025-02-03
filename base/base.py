from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from data_loader import DataLoader
from SingletonMeta import SeleniumDriver


class BasePage:
    def __init__(self):
        self.base_url = DataLoader().get_config_data('initial_setup')['base_url']
        self.wait = WebDriverWait(SeleniumDriver().get_driver(), DataLoader().get_config_data('initial_setup')['wait_time'], poll_frequency=1)
        self.action = ActionChains(SeleniumDriver().get_driver())

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def open(self):
        return SeleniumDriver().get_driver().get(self.base_url)

    def is_opened(self):
        return True if len(self.wait.until(EC.visibility_of_any_elements_located((By.XPATH, f'//{self.TAG}[contains(text(), "{self.UNIQUE_TEXT}")]')))) > 0 else False
