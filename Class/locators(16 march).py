'''
Xpath
Traversing
->Forward ----- > we use / or // , in this we fetch from parent to children
->Backward ----> we use /inp/.. , in this we fetch from children to parent


Backward Traversing steps :
step 1-> identify the static element
step 2-> move to common parent (backward)
step 3-> fetch the dynamic element

use of headless :
it is used to run the process in the backgroun without opening the browser
o.add_argument('--headless')

sibing concept :
->following sibling :
ex--   //td[text()="text"]//following-sibling::td[2]

->preceding sibling :
ex--   //td[text()="text"]//preceding-sibling::td[1]
'''

# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.maximize_window()

# driver.get("https://demoqa.com/webtables")
# salary =  driver.find_element(By.XPATH,'//td[text()="Cierra"]/..//td[5]')
# print(salary.text)
# driver.quit()

# driver.get("https://the-internet.herokuapp.com/tables")
# salary =  driver.find_element(By.XPATH,'//td[text()="Frank"]/..//td[4]')
# print(salary.text)
# driver.quit()







