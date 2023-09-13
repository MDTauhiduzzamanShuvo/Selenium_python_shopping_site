#Case_1
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://automationexercise.com/")
driver.maximize_window()

verify_homepage = driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]")

print(verify_homepage.is_displayed())
  #print(verify_homepage.is_selected())
  #print(verify_homepage.is_enabled())

driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]").click()

verify_all_products = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/h2")
time.sleep(3)
print(verify_all_products.is_displayed())
     #print(verify_all_products.is_selected())
     #print(verify_all_products.is_enabled())

driver.find_element(By.XPATH, "//input[@id='search_product']").send_keys("T-Shirt")
driver.find_element(By.XPATH, "//button[@id='submit_search']").click()

search_products = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/h2")
time.sleep(2)
print(search_products.is_displayed())

if driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/p").is_displayed():
    print("Product related to search is visible")
else:
    print("Failed")


time.sleep(5)
driver.close()




