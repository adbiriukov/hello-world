from selenium import webdriver
import time
import allure
from amazon_web_elements import WebElements


class TestAddToCart:
    @allure.story('Cart')
    @allure.severity('Critical')
    def test_add_to_cart(self):
        """
        1. Open main page
        2. Search anything
        3. Open first good
        4. Click add to cart 3 times
        5. Check that in cart 3 items
        """
        driver = webdriver.Chrome(executable_path=WebElements.path_google_chrome)
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(WebElements.url_main)
        driver.find_element(*WebElements.search_field).send_keys('cell phone')
        driver.find_element_by_id(WebElements.search_field).submit()
        driver.find_element_by_xpath(WebElements.xpath_first_search_output).click()

        x = 0
        while x < 3:
            driver.find_element_by_id(WebElements.id_add_to_cart).click()
            driver.back()
            x += 1
        driver.get(WebElements.url_main)
        assert driver.find_element_by_id('nav-cart').get_attribute('aria-label') == '3 items in cart'
