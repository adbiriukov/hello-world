from selenium import webdriver
import time
import allure
import amazon_web_elements


class TestAddToCart:
    @allure.story('Cart')
    @allure.severity('Critical')
    def test_add_to_cart(self):
        """
        1. Open main page
        2. Search anything
        3. Open first good
        4. Click add to cart
        5. Check that proceed to checkout appeared
        :return:
        """
        driver = webdriver.Chrome(executable_path=amazon_web_elements.path_google_chrome)
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(amazon_web_elements.url_main)
        driver.find_element_by_id(amazon_web_elements.id_search_box).send_keys('cell phone')
        driver.find_element_by_id(amazon_web_elements.id_search_box).submit()
        driver.find_element_by_xpath(amazon_web_elements.xpath_first_search_output).click()
        driver.find_element_by_id(amazon_web_elements.id_add_to_cart).click()
        time.sleep(5)
        driver.find_element_by_id(amazon_web_elements.id_cart_proceed_to_checkout).is_displayed()
