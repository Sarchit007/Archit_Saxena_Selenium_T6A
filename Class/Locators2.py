from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

# Another syntax for CSS SELECTORS -> "#" for ID and "." for CLASSNAME
# driver.get("https://demoqa.com/text-box")
# driver.find_element(By.CSS_SELECTOR, "input#userName").send_keys("hehehe")



# 8 XPATH -> XML PATH
'''
-> We can traverse backward or forward
-> Locate elements based on text and attribute
-> These are used for dynamic elements

Is of two types
1. Absolute -> Starts with "/" -> from root
2. Relative -> Starts with "//" -> directly jump to that element
'''

# //tagname[@attribute = "value"]

# driver.get("https://demoqa.com/text-box")
# driver.find_element(By.XPATH, '//input[@placeholder="Full Name"]').send_keys("hehehehe")
# driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

# If we want to find by some part of attribute value
# We can give full or partial value of attribute's value
# driver.get("https://amazon.in/")
# sleep(4)
# driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search Amazon')]").send_keys("Shirt")

# If we want to find by some part of text or full text
driver.get("https://amazon.in/")
sleep(4)

# Using text - text() ->
driver.find_element(By.XPATH,'//a[contains(text(),"Mobiles")]').click()

# Another syntax - "."
driver.find_element(By.XPATH,'//a[contains(.,"Mobiles")]').click()


# We can also find element using XPATH using indexing