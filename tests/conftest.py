import pytest
from SingletonMeta import SeleniumDriver


@pytest.fixture(scope='function', autouse=True)
def browser():
    SeleniumDriver().get_driver()
    yield SeleniumDriver().get_driver()
    SeleniumDriver.quit(SeleniumDriver().get_driver())

