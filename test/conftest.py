import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from configuration.ConfigProvider import ConfigProvider
from pages.DataAPI import DataAPI
from testdata.DataProvider import DataProvider

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser_name = ConfigProvider().get("ui", "browser_name")
        if browser_name == 'chrome':
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        browser.implicitly_wait(ConfigProvider().get_ui_timeout())
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() -> DataAPI:
    with allure.step("Вернуть DataAPI с данными"):
        return DataAPI(ConfigProvider().get_api_url())
    
@pytest.fixture
def test_data():
    with allure.step("Вернуть тестовые данные JSON"):
        return DataProvider()