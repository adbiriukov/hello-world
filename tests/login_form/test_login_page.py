import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()

    def test_facebook_link(self):
        self.driver.find_element_by_xpath('//*[@id="social-icons"]/a[2]/img').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.assertEqual(self.driver.current_url, 'https://www.facebook.com/OrangeHRM')


    def test_forget_password_option(self):
        self.driver.find_element_by_xpath('//*[@id="forgotPasswordLink"]/a').click()
        self.assertTrue(self.driver.find_element_by_id('securityAuthentication_userName').is_displayed())
        self.driver.find_element_by_id('btnCancel').click()
        self.assertTrue(self.driver.find_element_by_id('txtUsername').is_displayed())

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
