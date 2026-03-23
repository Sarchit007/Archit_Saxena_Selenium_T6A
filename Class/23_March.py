'''
action chain class
-create object
-store action
-perform

current window hande - on which window we are currenty on
window_hande - used for providing  the list of the tabs we have currently on the browser
switch_to_window(enter the tab)
'''
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.maximize_window()
# driver.get("https://amazon.in")
# sleep(3)
# ele = driver.find_element(By.ID, "twotabsearchtextbox")
# ele.send_keys("shoes for men")
# sleep(1)
# ele.send_keys(Keys.ENTER)
# sleep(3)
# driver.quit()

# driver.get("https://demoqa.com/text-box")
# ele=driver.find_element(By.XPATH,'//div[@class="col-md-9 col-sm-12"]/child::textarea[@id="currentAddress"]')
# ele.send_keys("Jaipur")
# ele.send_keys(Keys.CONTROL,"A")
# sleep(1)
# ele.send_keys(Keys.CONTROL,"c")
# sleep(2)
# p=driver.find_element(By.XPATH,'//div[@class="col-md-9 col-sm-12"]/child::textarea[@id="permanentAddress"]')
# p.send_keys(Keys.CONTROL,"v")
# sleep(2)
# driver.quit()

# driver.get("https://demoqa.com/buttons")
# el = driver.find_element(By.XPATH,'//button[text()="Click Me"]')
# sleep(1)
# el.click()
# el.click()
# sleep(2)
# actions = ActionChains(driver) # action is used to store the actions
# sleep(2)
# actions.click(el).perform() # .perform() will perform action
# sleep(2)
# dc = driver.find_element(By.XPATH,'//button[text()="Double Click Me"]')
# actions.double_click(dc).perform()
# sleep(1)
# rc = driver.find_element(By.XPATH,'//button[text()="Right Click Me"]')
# actions.context_click(rc).perform() #context_click is used to perform right click
# sleep(5)

# driver.get("https://amazon.in")
# driver.maximize_window()
# # driver.implicitly_wait(10)
# # el = driver.find_element(By.XPATH, '//a[@href="https://x.com/AmazonIN"]')
# sleep(5)
# actions = ActionChains(driver)
# # actions.scroll_to_element(el).pause(5).click(el).perform()
# # actions.scroll_by_amount(0,500).perform()
# # ori = driver.find_element(By.XPATH, '//div[@id="nav-belt"]')
# # origin = ScrollOrigin.from_element(ori)
# # actions.scroll_from_origin(origin, 0, 500).perform()
# f = driver.find_element(By.ID,"icp-nav-flyout")
# actions.move_to_element(f).perform()

# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# driver.maximize_window()
# actions = ActionChains(driver)
# sleep(5)
# driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("archit")
# el = driver.find_element(By.XPATH,'//button//img[@src="assets/img/Revamp/icon_eye_close.svg"]')
# sleep(3)
# actions.click_and_hold(el).pause(3).release().perform()


# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# actions = ActionChains(driver)
# sleep(2)
# drag = driver.find_element(By.XPATH,'//div[@id="draggable"]')
# dr = driver.find_element(By.XPATH,'//div[@id="droppable"]')
# actions.pause(3).drag_and_drop(drag,dr).perform()

driver.get("https://google.com")
sleep(5) # manually open 3 tabs
print(driver.current_window_handle)
sleep(5)
driver.switch_to.new_window()
driver.get("https://amazon.in")
sleep(6)
print(driver.window_handles)
print(driver.title)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)

driver.quit()

