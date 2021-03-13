@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        # you upload driver in "C:\program files\python\scripts" and don't specify location of the
        self.driver = webdriver.Chrome(
            executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        status = self.driver.find_element_by_xpath('//*[@id="divLogo"]/img').is_displayed()
        if status == True:
            assert True  # it's pytest assertion and if True meaning PASS
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listempleyees(self):
        pytest.skip('Skipping test.. Later i will implement..')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome(
            executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_id('txtUsername').send_keys('Admin ')
        self.driver.find_element_by_id('txtPassword').send_keys('admin1234')
        self.driver.find_element_by_id('btnLogin').click()
        message = self.driver.find_element_by_id('spanMessage')
        if message.text == "Invalid credentials":
            self.driver.close()
            assert True
        else:
            # allure Attach screenshot
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False