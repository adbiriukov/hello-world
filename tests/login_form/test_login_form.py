from selenium import webdriver
from elements.elements import LoginFormElements
import elements.constants as constants
import time
import pytest
import allure


@pytest.fixture()
def set_up():
    global driver
    driver = webdriver.Chrome(executable_path=constants.path_google_chrome)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
    yield
    driver.quit()


# Positive test
@allure.description("Login with correct login")
@allure.severity(severity_level="NORMAL")
def test_correct_login(set_up):
    # Test with correct login
    driver.find_element(*LoginFormElements.name).send_keys(LoginFormElements.correct_login)
    driver.find_element(*LoginFormElements.password).send_keys(LoginFormElements.correct_password)
    driver.find_element(*LoginFormElements.button).click()
    assert driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').is_displayed()


@allure.description("login by using cookies")
@allure.severity(severity_level="NORMAL")
def test_login_by_using_cookies(set_up):
    driver.delete_all_cookies()
    cookie = {'domain': 'opensource-demo.orangehrmlive.com', 'httpOnly': True, 'name': 'orangehrm', 'path': '/', 'secure': True, 'value': 'f4263d38b6a887a40dbaa7267fdabc40'}
    driver.add_cookie(cookie)
    driver.refresh()
    assert True == driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').is_displayed()

def test_logout(set_up):
    driver.find_element(*LoginFormElements.name).send_keys(LoginFormElements.correct_login)
    driver.find_element(*LoginFormElements.password).send_keys(LoginFormElements.correct_password)
    driver.find_element(*LoginFormElements.button).click()
    driver.find_element(*LoginFormElements.dashboard).is_displayed()
    driver.find_element(*LoginFormElements.welcome).click()
    driver.find_element(*LoginFormElements.logout).click()
    driver.find_element(*LoginFormElements.name).is_displayed()


# Negative tests
@allure.description("login with empty login and password fields")
@allure.severity(severity_level="NORMAL")
def test_empty_login_and_password(set_up):
    # login with empty login and password fields
    driver.find_element(*LoginFormElements.button).click()
    error_message = driver.find_element(*LoginFormElements.message)
    assert error_message.text == LoginFormElements.empty_username


@allure.description("login with empty password field")
@allure.severity(severity_level="NORMAL")
def test_empty_password_field(set_up):
    # login with password field
    driver.find_element(*LoginFormElements.name).send_keys(LoginFormElements.correct_login)
    driver.find_element(*LoginFormElements.button).click()
    error_message = driver.find_element(*LoginFormElements.message)
    assert error_message.text == LoginFormElements.empty_password


@allure.description("login with incorrect password")
@allure.severity(severity_level="NORMAL")
def test_incorrect_password(set_up):
    # login with incorrect password
    driver.find_element(*LoginFormElements.name).send_keys(LoginFormElements.correct_login)
    driver.find_element(*LoginFormElements.password).send_keys(LoginFormElements.incorrect_password)
    driver.find_element(*LoginFormElements.button).click()
    error_message = driver.find_element(*LoginFormElements.message)
    assert error_message.text == LoginFormElements.invalid_credentials
    time.sleep(3)
