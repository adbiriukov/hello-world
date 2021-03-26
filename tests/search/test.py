from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.amazon.com/')



search_field = driver.find_element_by_name('field-keywords')
search_field.clear()
search_field.send_keys('phone')
search_field.submit()

for x in range(1, 99):
    print(x)
    print(driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div["+str(x)+"]").is_displayed())

driver.quit()
