import time
from idlelib import browser

import signup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://automationexercise.com/")
driver.maximize_window()
verify_homepage = driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]")

print(verify_homepage.is_displayed())

time.sleep(3)
driver.find_element(By.XPATH,
                    "//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]").click()
driver.get("https://automationexercise.com/product_details/7")
driver.find_element(By.XPATH, "//body/section[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]/button[1]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//u[contains(text(),'View Cart')]").click()
time.sleep(5)
card_page = driver.find_element(By.XPATH, "//li[contains(text(),'Shopping Cart')]")
print(card_page.is_displayed())

driver.find_element(By.XPATH, "//a[contains(text(),'Proceed To Checkout')]").click()
time.sleep(3)

driver.find_element(By.XPATH, "//u[contains(text(),'Register / Login')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[2]").send_keys(
    "Abc")
driver.find_element(By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[3]").send_keys(
    "zequipoffessu1-1211111192195@yopmail.com")

time.sleep(4)

driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Abc")
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("def")
driver.find_element(By.CSS_SELECTOR, "#address1").send_keys("Abc")
driver.find_element(By.XPATH, "//input[@id='state']").send_keys("Dhk")
driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Dhk")
driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("1209")
driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("01711953127")

# account_create
driver.execute_script('document.querySelector("#form > div > div > div > div > form > button").click()')
time.sleep(3)

if driver.find_element(By.XPATH, "//b[contains(text(),'Account Created!')]"):
    print("ACCOUNT CREATED!")
else:
    print("Failed")

driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Proceed To Checkout')]").click()

if driver.find_element(By.XPATH, "//h2[contains(text(),'Address Details')]"):
    print("Address Verified")
else:
    print("Failed")

time.sleep(2)

driver.find_element(By.XPATH, "//body/section[@id='cart_items']/div[1]/div[6]/textarea[1]").send_keys("Abc")
driver.find_element(By.XPATH, "//a[contains(text(),'Place Order')]").click()
time.sleep(3)
driver.find_element(By.XPATH,
                    "//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys(
    "ABC")
time.sleep(3)

driver.find_element(By.XPATH,
                    "//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]").send_keys(
    "4321234567899876")
driver.find_element(By.XPATH,
                    "//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]").send_keys(
    "778")
driver.find_element(By.XPATH,
                    "//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[3]/div[2]/input[1]").send_keys(
    "02")
driver.find_element(By.XPATH,
                    "//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[3]/div[3]/input[1]").send_keys(
    "2027")
driver.find_element(By.CSS_SELECTOR, "#submit").click()

time.sleep(3)
if driver.find_element(By.XPATH,
                       "//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[3]/div[3]/input[1]"):
    print("Congratulations! Your order has been confirmed!")
else:
    print("Failed")

driver.find_element(By.XPATH,"//a[contains(text(),'Continue')]").click()

driver.close()