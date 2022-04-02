from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.freshworks.com/")

h1_element = driver.find_element(By.TAG_NAME, 'p')

print(h1_element.text)
driver.quit()
