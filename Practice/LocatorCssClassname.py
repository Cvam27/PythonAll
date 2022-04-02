from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://en-gb.facebook.com/")

driver.find_element(By.CSS_SELECTOR, '.inputtext._55r1._6luy').send_keys("Test")
driver.find_element(By.LINK_TEXT, 'Forgotten password?').click()
print("Pass")
driver.quit()
