import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture()
def driver():
    driver=WebDriver()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://fitpeo.com/")
    yield driver
    driver.quit()