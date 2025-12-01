import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.excel_utils import get_excel_data

test_data= get_excel_data(r"D:\Selenium with Python\DDT_User_Password.xlsx","Sheet1")

@pytest.mark.parametrize("username,password",test_data)
def test_login_ddt(setup,username,password):
    driver = setup

    driver.find_element(By.ID,"inputUsername").send_keys(username)
    driver.find_element(By.NAME,"inputPassword").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()





