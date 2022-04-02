from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://letskodeit.teachable.com/p/practice"


class pract():
    def test(self):
        driver.get(url)
        hidebtn = driver.find_elements(By.ID, 'hide-textbox')
        size = len(hidebtn)
        print(driver.title)


pract().test()
