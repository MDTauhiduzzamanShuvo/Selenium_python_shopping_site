import time

import click
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://automationexercise.com/")
driver.maximize_window()
verify_homepage = driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]")

print(verify_homepage.is_displayed())

time.sleep(3)
driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[8]/div/div[2]/ul/li/a").click()
time.sleep(2)
url_one = driver.current_url
print(url_one)

if not driver.current_url.find("product_details/7"):
    print("Failed")
else:
    print("Product detail is opened")

time.sleep(5)

#Sometime the add is comming out.
driver.get("https://automationexercise.com/product_details/7")



driver.find_element(By.TAG_NAME, "input").click()

time.sleep(3)
driver.find_element(By.TAG_NAME,"input").clear()
driver.find_element(By.TAG_NAME,"input").send_keys("4")
driver.find_element(By.XPATH,"//body/section[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]/button[1]").click()
time.sleep(5)

driver.find_element(By.XPATH,"//u[contains(text(),'View Cart')]").click()
time.sleep(4)

verify_number = driver.find_element(By.XPATH, "//button[contains(text(),'4')]")
print(verify_number.is_displayed())


time.sleep(2)
driver.close()

