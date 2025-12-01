from selenium import webdriver
from selenium.common import NoAlertPresentException, NoSuchElementException, StaleElementReferenceException, \
    TimeoutException, WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Enable incognito mode

# Launch Chrome with options
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

print("✅ Chrome launched in incognito mode")
print(driver.title)

driver.quit()

