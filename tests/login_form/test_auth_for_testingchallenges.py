from selenium import webdriver
import time
import elements.constants as constants
import pytest
import allure


@pytest.fixture()
def set_up():
    URL = "http://testingchallenges.thetestingmap.org/index.php"
    global driver
    driver = webdriver.Chrome(executable_path=constants.path_google_chrome)
    driver.implicitly_wait(30)
    driver.get(URL)
    yield
    driver.quit()


@allure.description("Login with Average value")
@allure.severity(severity_level="NORMAL")
def test_average_value(set_up):
    # 1 Average value
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('Name')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Minimum value")
@allure.severity(severity_level="NORMAL")
def test_minimum_value(set_up):
    # 2 Minimum value
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('f')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Maximum values")
@allure.severity(severity_level="NORMAL")
def test_maximum_values(set_up):
    # 3 Maximum values
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('aaaaaaaaaabbbbbbbbbbcccccccccc')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with more than maximum values")
@allure.severity(severity_level="NORMAL")
def test_more_than_maximum_values(set_up):
    # 4 More than maximum values
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('aaaaaaaaaabbbbbbbbbbccccccccccd')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Other chars then alphabetic")
@allure.severity(severity_level="NORMAL")
def test_login_with_other_chars_then_alphabetic(set_up):
    # 5 Other chars then alphabetic
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('1')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with used html tags")
@allure.severity(severity_level="NORMAL")
def test_used_html_tags(set_up):
    # 6 used html tags
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('<h1></h1>')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Basic XSS")
@allure.severity(severity_level="NORMAL")
def test_basic_xss(set_up):
    # 7 Basic XSS
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('<script></script>')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Space values at the beginning")
@allure.severity(severity_level="NORMAL")
def test_space_values_at_the_beginning(set_up):
    # 8 Space values at the beginning
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys(' Name')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Space in the middle")
@allure.severity(severity_level="NORMAL")
def test_space_in_the_middle(set_up):
    # 9 Space in the middle
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('Na me')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Space values at the end")
@allure.severity(severity_level="NORMAL")
def test_space_values_at_the_end(set_up):
    # 10 Space values at the end
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('Name ')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Non ASCII")
@allure.severity(severity_level="NORMAL")
def test_non_ASCII(set_up):
    # 11 Non ASCII
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('平仮名')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Space")
@allure.severity(severity_level="NORMAL")
def test_space(set_up):
    # 12 Space
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys(' ')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Empty value")
@allure.severity(severity_level="NORMAL")
def test_empty_value(set_up):
    # 13 Empty value
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Basic Sql injection")
@allure.severity(severity_level="NORMAL")
def test_basic_sql_injection(set_up):
    # 14 Basic Sql injection
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys("test'test;")
    first_name.submit()
    time.sleep(1)


@allure.description("Login with Missing css")
@allure.severity(severity_level="NORMAL")
def test_missing_css(set_up):
    # 15 Missing css
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('detailsoverviewnow.css')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with looked at the page source")
@allure.severity(severity_level="NORMAL")
def test_looked_at_the_page_source(set_up):
    # 16 looked at the page source
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('dfjwGGe82H43g3uRiy53h')
    first_name.submit()
    time.sleep(1)


@allure.description("Login with looked at the cookie value")
@allure.severity(severity_level="NORMAL")
def test_looked_at_the_cookie_value(set_up):
    # 17 looked at the cookie
    first_name = driver.find_element_by_id('firstname')
    first_name.send_keys('oi32jnxd42390slk345')
    first_name.submit()
    time.sleep(1)


# stop traffic by fiddler and change user right as admin to 1
# different browsers
# browser zoom in and out
# extremely big requests
# nasty words
