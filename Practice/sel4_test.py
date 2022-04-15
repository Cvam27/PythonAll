import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
Search_bar = driver.find_element(By.XPATH, "//input[@title='Search']")
Search_bar.send_keys("hello")
time.sleep(5)
Search_bar.find_element(By.XPATH, "//input[@title='Search']").send_keys("Test")
print(Search_bar.text)