import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider

class DataUi:
    def __init__(self, web_drv: WebDriver):
        self.url = ConfigProvider().get_ui_url()
        self.driver = web_drv

    @allure.step("Перейти на главную страницу")
    def go(self):
        self.driver.get(self.url)

    @allure.step("Нажать кнопку - в корзину")
    def order_product(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[id="tab1"]>div[class="news-list-container"]>div:nth-child(1)>div[class="tabs-item-info"]>button').click()

    @allure.step("Открыть корзину")
    def open_basket(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[class="bask_btn_right"]').click()

    @allure.step("Получить сумму покупок из корзины")
    def get_price(self) -> str:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="price_ti"]')))
        txt = self.driver.find_element(By.CSS_SELECTOR, 'span[class="price_ti"]').text
        return txt

    @allure.step("Получить сумму покупок из корзины с измененным количеством товара")    
    def increase_value(self) -> str:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="plus_prod"]')))
        self.driver.find_element(By.CSS_SELECTOR, 'span[class="plus_prod"]').click()
        txt = self.driver.find_element(By.CSS_SELECTOR, 'span[class="price_ti"]').text
        return txt
    
    @allure.step("Удалить добавленые товары из корзины") 
    def delete_product(self) -> str:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="delet_pr_bas"]')))
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="delet_pr_bas"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="body_order"]>h2')))
        txt = self.driver.find_element(By.CSS_SELECTOR, 'div[class="body_order"]>h2').text
        return txt