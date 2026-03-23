from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.nike.com/")
driver.maximize_window()
action = ActionChains(driver)

kids = driver.find_element(By.XPATH, "(//span[@role='button'])[4]")
action.move_to_element(kids).pause(3).perform()
kids.click()
sleep(2)

driver.switch_to.window(driver.window_handles[1])
shop = driver.find_element(By.XPATH, "//a[text()= 'Shop']")
action.scroll_to_element(shop).perform()
action.click(shop).perform()

sh = driver.find_element(By.XPATH, "(//div[@class= 'css-1sjxv95'])[13]")

action.scroll_to_element(sh).pause(2).perform()

action.click(sh).perform()

driver.switch_to.window(driver.window_handles[2])
sleep(2)
driver.find_element(By.XPATH, '//label[text()="UK 6 (EU 40)"]').click()
sleep(3)
driver.find_element(By.CLASS_NAME, "addToBagButtonContainer").click()


sleep(3)

driver.quit()