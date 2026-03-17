from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id = 'addNewRecordButton']").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Archit")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Saxena")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("arc@gmail.com")
driver.find_element(By.XPATH, "//input[@id='age']").send_keys("22")
driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("52000")
driver.find_element(By.XPATH, "//input[@id='department']").send_keys("AI ENG")
driver.find_element(By.XPATH, "//button[@id = 'submit']").click()

sala = driver.find_element(By.XPATH, "//td[text() = 'Archit']/..//td[5]")
print("The Salary is:",sala.text)

driver.quit()