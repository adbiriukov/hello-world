from selenium import webdriver
import pytest
import allure


@pytest.fixture()
def set_up():
    global driver
    driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    yield
    driver.quit()


@allure.description("Check that facebook link is working")
@allure.severity(severity_level="NORMAL")
def test_facebook_link(set_up):
    driver.find_element_by_xpath('//*[@id="social-icons"]/a[2]/img').click()
    driver.switch_to.window(driver.window_handles[-1])
    assert driver.current_url == 'https://www.facebook.com/OrangeHRM'


@allure.description("Check that 'Forgot your password?' link is working")
@allure.severity(severity_level="NORMAL")
def test_forget_password_option(set_up):
    driver.find_element_by_xpath('//*[@id="forgotPasswordLink"]/a').click()
    driver.find_element_by_id('securityAuthentication_userName').is_displayed()
    driver.find_element_by_id('btnCancel').click()
    driver.find_element_by_id('txtUsername').is_displayed()


@allure.description("Check that orangehrm link is working")
@allure.severity(severity_level="NORMAL")
def test_orangehrm_link(set_up):
    driver.find_element_by_xpath('//*[@id="footer"]/div[1]/a').click()
    driver.switch_to.window(driver.window_handles[-1])
    assert driver.current_url == 'https://www.orangehrm.com/'


@allure.description("Check that twitter link is working")
@allure.severity(severity_level="NORMAL")
def test_twitter_link(set_up):
    driver.find_element_by_xpath('//*[@id="social-icons"]/a[3]/img').click()
    driver.switch_to.window(driver.window_handles[-1])
    assert driver.current_url == 'https://twitter.com/orangehrm'


@allure.description("Check that youtube link is working")
@allure.severity(severity_level="NORMAL")
def test_youtube_link(set_up):
    driver.find_element_by_xpath('//*[@id="social-icons"]/a[4]/img').click()
    driver.switch_to.window(driver.window_handles[-1])
    assert 'https://www.youtube.com' in driver.current_url


@allure.description("Check that linkedin link is working")
@allure.severity(severity_level="NORMAL")
def test_youtube_link(set_up):
    driver.find_element_by_xpath('//*[@id="social-icons"]/a[1]/img').click()
    driver.switch_to.window(driver.window_handles[-1])
    assert driver.current_url == 'http://lawfilter.ertelecom.ru/'
