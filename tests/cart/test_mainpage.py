from selenium import webdriver
from elements.amazon_web_elements import WebElements
import allure
import pytest


@pytest.fixture()
def set_up():
    global driver
    driver = webdriver.Chrome(executable_path=WebElements.path_google_chrome)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    yield
    driver.quit()


@allure.description("Check for search field is displayed")
@allure.severity(severity_level="NORMAL")
def test_search_field_is_displayed(set_up):
    # check search field exists on  page
    assert True == driver.find_element(*WebElements.search_field).is_displayed()


@allure.description("Check for search field is enabled")
@allure.severity(severity_level="NORMAL")
def test_search_field_is_enabled(set_up):
    # check search field exists on  page
    assert True == driver.find_element(*WebElements.search_field).is_enabled()


@allure.description("Check for search field don't have attribute max length")
@allure.severity(severity_level="NORMAL")
def test_search_field_attribute(set_up):
    search_field = driver.find_element(*WebElements.search_field)
    assert None == search_field.get_attribute('maxlength')


@allure.description("Amazon Devices link is displayed/visible in the Home page footer")
@allure.severity(severity_level="NORMAL")
def test_my_account_link_is_displayed(set_up):
    account_link = driver.find_element_by_link_text('Amazon Devices')
    assert True == account_link.is_displayed()


@allure.description("All amazon banners is displayed")
@allure.severity(severity_level="NORMAL")
def test_count_of_promo_banners_images(set_up):
    # get promo banner list
    banner_list = driver.find_element(*WebElements.banner_list)

    # get images from the banner_list
    banners = banner_list.find_elements_by_tag_name('img')

    # check there are 5 banners displayed on the page
    assert 6 == len(banners)


@allure.description("Language option is displayed")
@allure.severity(severity_level="NORMAL")
def test_language_option_is_displayed(set_up):
    # check deliver to country is displayed
    assert True == driver.find_element(*WebElements.deliver_country).is_displayed()


@allure.description("By default shopping cart must be empty")
@allure.severity(severity_level="NORMAL")
def test_shopping_cart_empty_message(set_up):
    # check content of Shopping Cart is empty
    cart_status = driver.find_element(*WebElements.cart).get_attribute('aria-label')
    assert '0 items in cart' == cart_status
