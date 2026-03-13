'''
Find_element(locator_name, locator_value)
-> used for single element
->return single web element
->throws an exception when we are not able to find one

Find_elements(locator_name, locator_value)
->used for multiple elements
->return multiple web elements
->return an empty list if no element is found


->locator = address of an element
there are 8 types of locator :
-id                      -|
-name                    -|
                          |--->Direct Locator
-class name              -|
-tag name                -|

-link text                -|
                          -|-->text based
-partial link text        -|

-css selector             -|
                          -|-->Experation based Locators
-xpath                    -|

css selector : tagname[attribute= value]

element actions:
-click()
-send_keys("text") -- for entering user input
'''
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://amazon.com/")
# sleep(2)
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shirt")
# driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute").send_keys("shirt")
# sleep(2)
# driver.find_element(By.ID,"nav-search-submit-button").click()
# driver.get("https://demoqa.com/text-box")
# driver.find_element(By.ID,"userName").send_keys("Archit")
# driver.find_element(By.ID,"userEmail").send_keys("sarchit971@gmail.com")
# driver.find_element(By.ID,"currentAddress").send_keys("Jaipur")
# driver.find_element(By.ID,"permanentAddress").send_keys("Agra")
# sleep(2)
# driver.find_element(By.ID,"submit").click()

# username = driver.find_element(By.ID,"userName")
# username.send_keys("Archit")


# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://amazon.com/")
# sleep(2)
# # driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shirt")
# driver.find_element(By.LINK_TEXT,"Deals").click()
# sleep(2)
# driver.find_element(By.ID,"nav-search-submit-button").click()


# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://amazon.in/")
# sleep(2)
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shirt")
# driver.find_element(By.PARTIAL_LINK_TEXT,"Deals").click()
# sleep(2)
# driver.find_element(By.ID,"nav-search-submit-button").click()

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://amazon.in/")
sleep(2)
driver.find_element(By.LINK_TEXT,'Downloads').click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Deals").click()
sleep(2)

driver.maximize_window()
driver.close()
