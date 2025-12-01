from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver= driver

    def do_click(self,locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator)).click()

    def do_send_keys(self,locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self,locator):
        element= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        return element

    def is_visible(self,locator):
        element= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        return bool(element)

