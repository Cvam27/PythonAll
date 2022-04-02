from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


# def select_by_text(element, value):
#      slct = Select(element)
#      slct.select_by_visible_text(value)
#
# def select_by_val(element, value):
#     slct = Select(element)
#     slct.select_by_value(value)
#
# ele_country = driver.find_elements(By.ID, 'Form_submitForm_Country')
#
#
#
#
# # select_by_text(ele_country, 'Germany')
# # select_by_val(ele_country, 'India')
#
#
# slct = Select(ele_country)
# countrylist = slct.options
#
#
#
#
#
# ele_countrylist = driver.find_elements(By.ID, 'Form_submitForm_Country')
# for i in ele_countrylist:
#     print(i.text)
#     if i == "India":
#         i.click()
#         break
# # slct = Select(ele_country)
# # slct.select_by_value('India')
# # time.sleep(3)
# # slct.select_by_visible_text("Australia")
# # time.sleep(3)
# # slct.select_by_index(3)
# # time.sleep(3)
#
# # Deselect value0
# slct.deselect_by_index(3)

def options_in_dropdown(options, value):
    print(len(options))
    for ele in options:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


ele_without_select = driver.find_elements(By.XPATH, "//select[@id='Form_submitForm_Country']/option")

options_in_dropdown(ele_without_select, "France")
