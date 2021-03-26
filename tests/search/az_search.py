from selenium import webdriver
import allure
import pytest


@pytest.fixture()
def set_up():
    global driver
    driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://www.amazon.com/')
    yield
    driver.quit()


# @allure.description("Check for search field is displayed")
# @allure.severity(severity_level="Critical")
# @pytest.mark.parametrize('search_value, expected_count', [('phone', 'music'), ('results', 'results')])
# def test_search(set_up, search_value, expected_count):
#     """
#     1. Open main page
#     2. send value to the search field
#     3. 'result' is displayed on the page
#     """
#     search_field = driver.find_element_by_name('field-keywords')
#     search_field.clear()
#     search_field.send_keys(search_value)
#     search_field.submit()
#     result = driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]')
#     print(result.text)
#     assert expected_count in result.text


# @allure.description("Correction message is displayed")
# @allure.severity(severity_level="Normal")
# @pytest.mark.parametrize('search_value', ('ggle', 'sttar track'))
# def test_search(set_up, search_value):
#     """
#     1. Open main page
#     2. send value with error to the search field
#     3. Correction message is displayed
#     """
#     search_field = driver.find_element_by_name('field-keywords')
#     search_field.clear()
#     search_field.send_keys(search_value)
#     search_field.submit()
#     driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/span/div/div/h1[1]/span').is_displayed()


# @allure.description("Navigation back and forward")
# @allure.severity(severity_level="Normal")
# def test_search(set_up):
#     """
#     1. Open main page
#     2. Send value to the search field
#     3. Check driver title
#     4. Go back
#     5 Check driver title
#     6 Go forward
#     7 Check driver title
#     """
#     search_field = driver.find_element_by_name('field-keywords')
#     search_field.clear()
#     search_field.send_keys('google')
#     search_field.submit()
#     assert 'google' in driver.title
#     driver.back()
#     assert 'Online Shopping' in driver.title
#     driver.forward()
#     assert 'google' in driver.title

#
# @allure.description("Check that all 23 goods is displayed")
# @allure.severity(severity_level="Normal")
# def test_search(set_up):
#     """
#     1. Open main page
#     2. Send value to the search field
#     3. Check number of goods displayed
#     """
#     search_field = driver.find_element_by_name('field-keywords')
#     search_field.clear()
#     search_field.send_keys('phone')
#     search_field.submit()
#     # displayed_results = driver.find_elements_by_class_name('sg-col-inner')
#     # assert 54 == len(displayed_results)
#     for x in range(1, 24):
#         driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div[" + str(x) + "]").is_displayed()

@allure.description("Total results box is displayed")
@allure.severity(severity_level="Normal")
def test_search(set_up):
    """
    1. Open main page
    2. Send value to the search field
    3. Total results box is displayed
    """
    search_field = driver.find_element_by_name('field-keywords')
    search_field.clear()
    search_field.send_keys('phone')
    search_field.submit()
    driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]').is_displayed()
