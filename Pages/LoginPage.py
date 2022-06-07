from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Tests.ReadData import ReadData as RD
from Pages.DashboardPage import DashboardPage


class LoginPage(BasePage):

    # By Locators used in Class

    # using ID as Locator
    UserName = (By.ID, "txtUsername")
    Password = (By.ID, "txtPassword")
    LoginBtn = (By.ID, "btnLogin")

    # using XPATH as locator
    UserDetails = (By.XPATH, "//div/span")

    # using CSS Selector
    ForgetPassword = (By.CSS_SELECTOR, "div[id='forgotPasswordLink']")

    # Constructor of class - to call Super Class constructor
    def __init__(self, driver):
        super().__init__(driver)
        #super().__init__()
        self.driver.get(RD.base_url)

    '''Page Actions function'''

    '''
        Function  : To Check title is correct
        Input     : Expected title
        Output    : Actual title
    '''
    def get_login_page_title(self, title):
        return self.get_title(title)

    ''' To Check forget password Text is visible'''
    def is_forget_password_link_exist(self):
        return self.is_visible(self.ForgetPassword)

    ''' This for login to Site with provided value'''
    def do_login(self, username, password):
        self.do_send_keys(self.UserName, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.LoginBtn)
        text = self.driver.find_element(By.CSS_SELECTOR, "span#spanMessage").text
        return text

    '''To get Screen user and Password details'''
    def get_user_details(self):
        text = self.get_element_text(self.UserDetails)
        user_and_password = text[1, -1]
        user_text, password_text = user_and_password.split("|")
        _, username = user_text.split(":")
        _, password = password_text.split(":")
        return username, password

    ''' This for login to Site with values on Screen'''
    def do_login_with_screen_value(self):
        self.do_send_keys(self.UserName, self.get_user_details()[0])
        self.do_send_keys(self.Password, self.get_user_details()[1])
        self.do_click(self.LoginBtn)
        # self.do_login(self.get_user_details()[0], self.get_user_details()[1])
        welcometext = self.driver.find_element(By.CSS_SELECTOR, "a#welcome").text

        return welcometext
