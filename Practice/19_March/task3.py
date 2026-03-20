from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get("https://demowebshop.tricentis.com/register")
driver.find_element(By.ID,"gender-male").click()
driver.find_element(By.ID,"FirstName").send_keys("Archit")
driver.find_element(By.ID,"LastName").send_keys("Saxena")
driver.find_element(By.ID,"Email").send_keys("A@gmail.com")
driver.find_element(By.ID,"Password").send_keys("123456")
driver.find_element(By.ID,"ConfirmPassword").send_keys("123456")
driver.find_element(By.ID,"register-button").click()

driver.quit()