from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from data_loader import DataLoader


class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class SeleniumDriver(metaclass=SingletonMeta):
    def add_options(self, options):
        for option in options.values():
            self.__options.add_argument(option)

    def __setup_driver(self):
        config_data = DataLoader()
        options = config_data.get_config_data('options')

        match config_data.get_config_data('initial_setup')['browser']:
            case 'chrome':
                self.__options = webdriver.ChromeOptions()
                self.add_options(options)
                self.__options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
                self.__driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=self.__options)

    def get_driver(self):
        if not hasattr(self, "_SeleniumDriver__driver"):
            self.__setup_driver()
        return self.__driver

    def quit(self):
        if hasattr(self, "__driver"):
            self.__driver.quit()
            cls = self.__class__
            if cls in cls.__class__.__instances:
                del cls.__class__.__instances[cls]