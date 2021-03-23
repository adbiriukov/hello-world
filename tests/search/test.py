from selenium import webdriver
import allure
import pytest
import time

driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.amazon.com/')



search_field = driver.find_element_by_name('field-keywords')
search_field.clear()
search_field.send_keys('google')
search_field.submit()

a = driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]')
assert '1-48' in a.text

driver.quit()
