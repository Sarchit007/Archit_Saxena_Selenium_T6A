from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/restaurants?category=1")
sleep(3)
driver.find_element(By.XPATH,'//input[@class="sc-dBfaGr dyyfrm"]' ).send_keys("dosa")
driver.find_element(By.XPATH,'//input[@class="sc-dBfaGr dyyfrm"]' ).click()
sleep(3)
sug = driver.find_elements(By.XPATH,'//div[@class="sc-glUWqk GrjUP"]' )
sleep(2)
sug[2].click()

driver.quit()