import pytest
from SingletonMeta import SeleniumDriver


@pytest.fixture(scope='function', autouse=True)
def browser():
    driver = SeleniumDriver().get_driver()
    yield driver
    SeleniumDriver.quit(driver)

