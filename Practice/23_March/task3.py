from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.flipkart.com/")

actions = ActionChains(driver)

sleep(3)

# Myntra
my = driver.find_element(By.XPATH, '//a[contains(@href,"myntra")]')
actions.scroll_to_element(my).pause(2).perform()
my.click()

sleep(3)

# Cleartrip
cl = driver.find_element(By.XPATH, '//a[contains(@href,"cleartrip")]')
cl.click()

sleep(3)

# Shopsy
sh = driver.find_element(By.XPATH, '//a[contains(@href,"shopsy")]')
sh.click()

sleep(5)
print(driver.window_handles)
windows = driver.window_handles
for w in windows:
    driver.switch_to.window(w)
    sleep(2)
    print("URL:", driver.current_url)
    print("Title:", driver.title)
driver.quit()