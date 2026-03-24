'''
i frame :
methods :
-by indexing
-by name
-by web element(locator)
'''

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common import alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
driver.maximize_window()
# driver.get(r"C:\Users\sarch\OneDrive\Desktop\T6A_Selenuim\Class\page.html")


#by using index
# driver.implicitly_wait(10)
# driver.find_element(By.ID,"in1").send_keys("hello")
# driver.switch_to.frame(0)
# driver.find_element(By.ID,"in2").send_keys("hello2")
# driver.switch_to.frame(0)
# driver.find_element(By.ID,"in3").send_keys("hello3")


#by using NAME
# driver.implicitly_wait(10)
# driver.find_element(By.ID,"in1").send_keys("hello")
# driver.switch_to.frame("f2")
# driver.find_element(By.ID,"in2").send_keys("hello2")
# driver.switch_to.frame("f3")
# driver.find_element(By.ID,"in3").send_keys("hello3")

#by ID
# driver.implicitly_wait(10)
# driver.find_element(By.ID,"in1").send_keys("hello")
# driver.switch_to.frame("faah1")
# driver.find_element(By.ID,"in2").send_keys("hello2")
# driver.switch_to.frame("faah2")
# driver.find_element(By.ID,"in3").send_keys("hello3")



# driver.implicitly_wait(10)
# driver.find_element(By.ID,"in1").send_keys("hello")
# el = driver.find_element(By.XPATH,"")
# driver.switch_to.frame("faah1")
# driver.find_element(By.ID,"in2").send_keys("hello2")
# driver.switch_to.frame("faah2")
# driver.find_element(By.ID,"in3").send_keys("hello3")


# driver.get("https://x.com/")
# driver.find_element(By.XPATH,'//iframe[@src="https://accounts.google.com/gsi/button?theme=outline&size=large&shape=circle&logo_alignment=center&text=signup_with&width=300&is_fedcm_supported=true&client_id=49625052041-kgt0hghf445lmcmhijv46b715m2mpbct.apps.googleusercontent.com&iframe_id=gsi_699216_286367&cas=MfbZ2y7c0Q3DQ0xNhFJ49nGi38NBlzcN5R6rRtaHfgE&hl=en"]').click()


#by ID
# driver.implicitly_wait(10)
# driver.find_element(By.ID,"in1").send_keys("hello")
# driver.switch_to.frame("faah1")
# driver.find_element(By.ID,"in2").send_keys("hello2")
# driver.switch_to.parent_frame()
# driver.find_element(By.ID,"in1").clear()
# driver.find_element(By.ID,"in1").send_keys("i'm back")


# # driver.implicitly_wait(10)
# driver.find_element(By.ID,"in1").send_keys("hello")
# el = driver.find_element(By.XPATH,"")
# driver.switch_to.frame("faah1")
# driver.find_element(By.ID,"in2").send_keys("hello2")
# driver.switch_to.frame("faah2")
# driver.find_element(By.ID,"in3").send_keys("hello3")

# driver.implicitly_wait(10)
# driver.find_element(By.ID,"in1").send_keys("hello")
# driver.switch_to.frame("faah1")
# driver.find_element(By.ID,"in2").send_keys("hello2")
# driver.switch_to.frame("faah2")
# driver.find_element(By.ID,"in3").send_keys("hello3")
# driver.switch_to.default_content()
# driver.find_element(By.ID,"in1").clear()
# driver.find_element(By.ID,"in1").send_keys("i'm back")


# driver.get("https://testautomationpractice.blogspot.com/")
# driver.find_element(By.XPATH,'//button[@id="alertBtn"]').click()
# driver.find_element(By.XPATH,'//button[@id="promptBtn"]').click()
# sleep(2)
# driver.switch_to.alert.accept()
# driver.switch_to.alert.send_keys("hello")
# sleep(3)
# driver.switch_to.alert.accept()

# driver.get("https://www.python.org/downloads/")
# driver.find_element(By.XPATH, '(//a[. = "Python 3.14.3"])[4]').click()