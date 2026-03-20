from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.implicitly_wait(5)
links=driver.find_elements(By.XPATH,"//h2[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal']")
print(links)
print(len(links))
for link in links:
    print(link.text)

print("6th product name is: ", links[5].text)
links[5].click()
driver.quit()