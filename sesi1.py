from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\chrome_driver\chromedriver.exe')
driver.maximize_window()
driver.get('https://google.com')
driver.close()