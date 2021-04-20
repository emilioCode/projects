from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Owner\Desktop\projects\chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(5)
driver.close()