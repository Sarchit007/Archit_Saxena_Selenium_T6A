from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options=o)
driver.get("https://www.zomato.com/login")
sleep(3)

driver.switch_to.frame(0)
sleep(2)
su=driver.find_element(By.XPATH,"(//iframe[@title='Sign in with Google Button'])[1]")
sleep(2)
driver.switch_to.frame(su)
# sleep(2)
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
sleep(2)
driver.switch_to.window(driver.window_handles[1])
sleep(5)