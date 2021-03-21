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


@allure.description("Check for search field is displayed")
@allure.severity(severity_level="NORMAL")
@pytest.mark.parametrize('search_value, expected_count', [('phone', 'music'), ('results', 'results')])
def test_search(set_up, search_value, expected_count):
    search_field = driver.find_element_by_name('field-keywords')
    search_field.clear()
    search_field.send_keys(search_value)
    search_field.submit()
    result = driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]')
    print(result.text)
    assert expected_count in result.text
