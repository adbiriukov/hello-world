from selenium import webdriver
import time
import allure
import constants


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
        driver = webdriver.Chrome(executable_path=constants.path_google_chrome)
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(constants.url_main)
        driver.find_element_by_id(constants.id_search_box).send_keys('cell phone')
        driver.find_element_by_id(constants.id_search_box).submit()
        driver.find_element_by_xpath(constants.xpath_first_search_output).click()

        x = 0
        while x < 3:
            driver.find_element_by_id(constants.id_add_to_cart).click()
            driver.back()
            x += 1
        driver.get(constants.url_main)
        assert driver.find_element_by_id('nav-cart').get_attribute('aria-label') == '3 items in cart'
