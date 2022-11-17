from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
