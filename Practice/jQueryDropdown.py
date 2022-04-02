import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")


def select_jquery_value(option_list, value):
    for ele in option_list:
        print(ele.text)
        for k in range(len(value)):
            if ele.text == value[k]:
                ele.click()
                break


driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(2)

ddList = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list = ['choice 1', 'choice 2', 'choice 3']
select_jquery_value(ddList, value_list)

# select_jquery_value(ddList, 'choice 2')
# select_jquery_value(ddList, 'choice 3')
# select_jquery_value(ddList, 'choice 4')

# for ele in ddList:
#     print(ele.text)
#     if ele.text == "choice 1":
#         ele.click()
#         break


time.sleep(2)
driver.quit()
