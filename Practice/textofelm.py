from selenium import webdriver
from webdriver_manager.chrome import *

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://letskodeit.teachable.com/p/practice"

driver.get(url)
