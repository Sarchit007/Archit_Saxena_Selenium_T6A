from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.implicitly_wait(15)


driver.find_element(By.ID, "singleFileInput").send_keys(r"C:\Users\sarch\OneDrive\Desktop\T6A_Selenuim\Practice\19_March\peter-olexa-mxIGWk111u0-unsplash.jpg")
l = [r"C:\Users\sarch\OneDrive\Desktop\T6A_Selenuim\Practice\19_March\shea-rouda-Ete0zMKPWys-unsplash.jpg", r"C:\Users\sarch\OneDrive\Desktop\T6A_Selenuim\Practice\19_March\jordan-qWHy3Qz_M7I-unsplash.jpg"]
for i in range(0,len(l)):
    driver.find_element(By.ID, "multipleFilesInput").send_keys(l[i])