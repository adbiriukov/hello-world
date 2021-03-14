# welcome_text_elm = driver.find_element_by_tag_name("h1")
# welcome_text = welcome_text_elm.text
#
# assert "Congratulations! You have successfully registered!" == welcome_text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from elements.amazon_web_elements import WebElements
import allure
import pytest


@pytest.fixture()
def set_up():
    global driver
    driver = webdriver.Chrome(executable_path=WebElements.path_google_chrome)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://formy-project.herokuapp.com/form')
    yield
    driver.quit()

@allure.description("Check for search field is displayed")
@allure.severity(severity_level="NORMAL")
def test_positive_registration_form(set_up):
    driver.find_element_by_id('first-name').send_keys('test1')
    driver.find_element_by_id('last-name').send_keys('test2')
    driver.find_element_by_id('job-title').send_keys('tester')
    driver.find_element_by_id('radio-button-3').click()
    driver.find_element_by_id('checkbox-1').click()
    driver.find_element_by_id('select-menu').click()
    driver.find_element_by_xpath('//*[@id="select-menu"]/option[3]').click()
    driver.find_element_by_id('datepicker').send_keys('01/11/2020')
    driver.find_element_by_id('datepicker').send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/form/div/div[8]/a').click()
    # wait response
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/div')))
    # check
    assert driver.find_element_by_xpath('/html/body/div/div').text == 'The form was successfully submitted!'





