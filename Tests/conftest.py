from selenium import webdriver
import pytest


@pytest.fixture
def setup():
    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/locatorspractice/")
    yield driver
    driver.quit()