from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class DashboardPage(BasePage):
    # 'a#welcome'
    # Using CSS selector to get account name
    ACCOUNT_NAME = (By.CSS_SELECTOR, "a#welcome")

    def __init__(self, driver):
        super().__init__(driver)

    def get_dashboard_title(self, title):
        return self.get_title(title)

    ''' Checking if account name is visible, if yes, then return the text'''
    def get_account_name(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)
