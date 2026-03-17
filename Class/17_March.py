# implicit wait (also known as global wait) - here time is not wasted like sleep
# give implicit wait
# if given for 15 sec then each half sec it will check is the element present or not

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# driver.maximize_window()
#
# driver.find_element(By.TAG_NAME, 'button').click()
#
# driver.implicitly_wait(10)
# print(driver.find_element(By.XPATH, '(//h4)[2]').text)
#

# driver.get("https://www.decathlon.in/")
# driver.find_element(By.XPATH,'//a[contains(@href,"https://www.decathlon.in/shop/Winter-Collection")]').click()
# a =driver.find_element(By.XPATH,'//a[contains(@href,"/p/8862712_migration/kids-warm-and-waterproof-winter-hiking-jacket-sh100-3-5-c-7-15-years")]').click()
# print(a.text)




driver.quit()