from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
actions = ActionChains(driver)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH,'//a[@href="/javascript_alerts"]').click()
sleep(2)
#for simple alert
driver.find_element(By.XPATH,'//button[text()="Click for JS Alert"]').click()
sleep(2)
al=driver.switch_to.alert
print(al.text)
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
#for JS confirm
driver.find_element(By.XPATH,'//button[text()="Click for JS Confirm"]').click()
sleep(2)
al2=driver.switch_to.alert
print(al2.text)
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
#for js prompt
driver.find_element(By.XPATH,'//button[text()="Click for JS Prompt"]').click()
sleep(2)
driver.switch_to.alert.send_keys("hello")
sleep(1)
al2=driver.switch_to.alert
print(al2.text)
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
driver.quit()


