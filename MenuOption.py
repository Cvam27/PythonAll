from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://ciceroni.in/")
action = ActionChains(driver)
menu = driver.find_element_by_xpath("//a[@class = 'dropbtna']")
action.move_to_element(menu).perform()

print(driver.title)
driver.quit()
