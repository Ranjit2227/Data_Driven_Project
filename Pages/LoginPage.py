from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """Locators of Login Page"""
    username_input= (By.XPATH,"//input[@name='username']")
    password_input= (By.XPATH,"//input[@name='password']")
    login_btn= (By.XPATH,"//button[normalize-space()='Login']")
    forgot_link= (By.XPATH,"//p[normalize-space()='Forgot your password?']")
    logout_btn= (By.PARTIAL_LINK_TEXT,"Logout")


    """ create consructor and super """
    def __init__(self,driver):
        super().__init__(driver)

    """ actions """

    def login_to_application(self,username,password):
        self.do_send_keys(self.username_input,username)
        self.do_send_keys(self.password_input,password)
        self.do_click(self.login_btn)

    def logout_from_application(self):
        self.do_click(self.logout_btn)


