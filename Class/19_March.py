'''
finding multiple elements --> we use find_elements

is displayed()
is displayed()
is displayed()


'''


# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from time import sleep
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
# driver.get("https://google.com/")
# driver.implicitly_wait(10)
#
# link = driver.find_elements(By.TAG_NAME,"a")
# print(link)
#
# for l in link:
#     print(l.text)
#
# driver.quit()



# driver.get("https://facebook.com/")
# driver.implicitly_wait(10)

#
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("watch")
# driver.find_element(By.ID,"nav-search-submit-button").click()
# prod = driver.find_elements(By.CLASS_NAME,"a-size-base-plus.a-spacing-none.a-color-base.a-text-normal")
# print(len(prod))
# print(prod[4].text)

# for i in prod:
#     print(i.text)


# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("watch")
# driver.find_element(By.ID,"nav-search-submit-button").click()

# driver.get("https://amazon.in/")
# driver.implicitly_wait(10)

# ele = driver.find_elements(By.XPATH,'//div[@id="nav-main"]//a')
#
# for i in ele:
#     if i.text != "":
#         print(i.text," : ",i.get_attribute("href"))

# btn = driver.find_element(By.XPATH,'//div[@aria-label="Log in"]')
# print(btn.is_displayed())
#
# driver.quit()

#
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
# driver.implicitly_wait(15)
#
# btn1 = driver.find_element(By.XPATH,'(//input[@type="checkbox"])[1]')
# print(btn1.is_selected())
#
# btn2 = driver.find_element(By.XPATH,'(//input[@type="checkbox"])[2]')
# print(btn2.is_selected())

# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shoes")

#
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from time import sleep
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
# driver.get("https://demoqa.com/automation-practice-form")
# driver.implicitly_wait(10)

# driver.find_element(By.ID,"firstName").send_keys("Archit")
# driver.find_element(By.ID,"lastName").send_keys("Saxena")
# driver.find_element(By.ID,"userEmail").send_keys("a@gmail.com")
# driver.find_element(By.CLASS_NAME,"form-check.form-check-inline").click()
# driver.find_element(By.ID,"userNumber").send_keys("7895*****")
# driver.find_element(By.ID,"dateOfBirthInput").send_keys("02 Jan 2004")
# driver.find_element(By.ID,"subjectsInput").send_keys("Math")
# driver.find_element(By.ID,"hobbies-checkbox-1").click()
# driver.find_element(By.ID,"uploadPicture").send_keys(r"C:\Users\sarch\OneDrive\Desktop\T6A_Selenuim\Practice\Problem_Statement_1.md")
# driver.find_element(By.ID,"currentAddress").send_keys("Jaipur")
# driver.quit()




# driver.get("https://demoqa.com/automation-practice-form")
# driver.maximize_window()
# driver.find_element(By.ID, "firstName").send_keys("Aditya")
# driver.find_element(By.ID, "lastName").send_keys("Paliwal")
# driver.find_element(By.ID, "userEmail").send_keys("asd@asd.com")
# driver.find_element(By.XPATH, '//input[@id="gender-radio-1"]').click()
# driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys("0987654321")
# driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
# mon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//option[@value="7"]')))
# mon.click()
# driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
# dat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[. = "15"]')))
# dat.click()
# driver.find_element(By.XPATH, '(//div[@class="form-check form-check-inline"])[5]').click()
# driver.find_element(By.XPATH, '(//div[@class="form-check form-check-inline"])[6]').click()
# driver.find_element(By.XPATH, '//input[@id="uploadPicture"]').send_keys(r"C:\Users\ADITYA\Downloads\Problem_Statement_1.md")
# # driver.find_element(By.XPATH, '//input[@id="subjectsInput"]').send_keys("Maths")
# driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]').send_keys("why d you nedd")
# driver.find_element(By.XPATH, '//button[@id="submit"]').click()


# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
# driver.get("https://www.naukri.com/")
# driver.maximize_window()
# driver.find_element(By.ID,"register_Layer").click()
# driver.find_element(By.ID,"name").send_keys("Archit")
# driver.find_element(By.ID,"email").send_keys("sarchit971@gmail.com")
# driver.find_element(By.ID,"password").send_keys("pass")


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
