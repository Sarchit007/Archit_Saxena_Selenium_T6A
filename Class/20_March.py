
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep


from selenium.webdriver.support.select import Select

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
# driver.get(r"C:\Users\sarch\OneDrive\Desktop\T6A_Selenuim\Class\E22_Dropdowns.html")
# d = driver.find_element(By.ID, "state")
# option = Select(d)

# option.select_by_visible_text("Kerala")
# option.select_by_index(3)
# sleep(3)


# driver.get("https://www.amazon.in")
# sleep(3)
# driver.find_element(By.ID, "twotabsearchtextbox").send_keys("shoes for men")
# sleep(3)
# sug = driver.find_elements(By.XPATH,'//div[@class="s-suggestion-container"]')
# sleep(2)
# sug[2].click()

# for i in sug:
#     print(i.text)

