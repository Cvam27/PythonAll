from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

# linkElement = driver.find_elements(By.TAG_NAME, 'a')
#
# print(len(linkElement))
#
# for i in linkElement:
#     print(i.text)
#     print(i.get_attribute('href'))

imgList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imgList))

driver.quit()
