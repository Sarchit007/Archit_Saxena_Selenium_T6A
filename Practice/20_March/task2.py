from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.bmrc.co.in/")
sleep(2)
driver.find_element(By.XPATH,'//i[@class="fa fa-globe"]').click()
sleep(2)
d = driver.find_element(By.XPATH,'(//select[@class="form-control select fare-selects"])[1]')
option = Select(d)
option.select_by_index(3)
sleep(2)
f = driver.find_element(By.XPATH,'(//select[@class="form-control select fare-selects"])[2]')
option = Select(f)
option.select_by_index(5)
driver.find_element(By.XPATH,'//button[@class="app-btn-box"]').click()
sleep(5)
driver.quit()