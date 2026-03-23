from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(3)
action=ActionChains(driver)

#hover:
el = driver.find_element(By.XPATH,'//button[@class="dropbtn"]')
sleep(2)
action.move_to_element(el).perform()

#Double click:
el = driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
sleep(2)
action.double_click(el).perform()

#Drag and Drop:
s = driver.find_element(By.XPATH,'//div[@id="draggable"]')
d = driver.find_element(By.XPATH,'//div[@id="droppable"]')
action.pause(2).drag_and_drop(s,d).perform()

driver.quit()
