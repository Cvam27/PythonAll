import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://cloud.tenable.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(50)
driver.maximize_window()


class addFilterInTagRule():
    def login(self):
        driver.get(url)
        time.sleep(10)
        driver.find_element(By.XPATH, "//input[@class = 'required login-username']")
        driver.find_element(By.XPATH, "//input[@class = 'required login-password']").send_keys("Tenable@123!")
        driver.find_element(By.ID, "sign-in").click()


    def navigationBar(self):
        driver.find_element(By.XPATH, "//*[@id='main-app-container']/div[1]/button").click()
        driver.find_element(By.XPATH,
                            "//*[@id='main-app-navigation']/div[1]/div[1]/div[2]/div/div/div/div[6]/div/div").click()

    def clickTagging(self):
        driver.find_element(By.XPATH, "//*[@id='page-content-body-content']/div/div[2]/div/div[2]/div").click()
        time.sleep(5)

    def createTagClick(self):
        driver.find_element(By.XPATH, "//*[@id='template-header']/div/div[3]/div/button").click()
        time.sleep(10)

    def ruleToggle(self):
        driver.find_element(By.XPATH,
                            "//*[@id='template-content']/div/div[3]/div/div/form/fieldset[2]/legend/div/div[2]/div/div/div/div/div/div/div").click()
        time.sleep(5)

    def clickAddFilter(self):
        for count in range(1100):
            driver.find_element(By.XPATH, "//button[@kind = 'secondary']").click()
            print(count)
            time.sleep(1)


ff = addFilterInTagRule()
ff.login()
ff.navigationBar()
ff.clickTagging()
ff.createTagClick()
ff.ruleToggle()
ff.clickAddFilter()
