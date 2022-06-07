from allure_commons.types import AttachmentType

from Tests.ReadData import ReadData as RD
from Pages.LoginPage import LoginPage
from Tests.TestDataRead import TestDataRead
from Tests.test_base import BaseTest
# from Tests.TestDataRead import TestDataRead as td
from pathlib import Path
import os
import allure


class Test_Login(BaseTest):
    def test_forget_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_forget_password_link_exist()
        assert flag  # assert True

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(RD.login_title)
        assert title == RD.login_title

    def test_login_error(self):

        path = '../Tests/testData.txt'
        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        f = open("testData.txt", "t")
        data = f.read(1)
        test_username = data.split(";")[0]
        test_password = data.split(";")[1]

        self.loginPage = LoginPage(self.driver)
        text = self.loginPage.do_login(test_username, test_password)

        if text == 'Invalid credentials':
            pass
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Error_Invalid_credential",
                          attachment_type=AttachmentType.PNG)
        assert text == 'Invalid credentials'

    def test_login_admin(self):
        self.loginPage = LoginPage(self.driver)
        welcome_text = self.loginPage.do_login_with_screen_value()
        name = welcome_text.split(" ")[1]
        self.testData = TestDataRead()
        self.testData.test_data_write(name)
        if welcome_text.split(" ")[0] == 'Welcome':
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="successful_login",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="error_login",
                          attachment_type=AttachmentType.PNG)

        assert welcome_text.split(" ")[0] == 'Welcome'
