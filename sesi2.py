from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\chrome_driver\chromedriver.exe')
driver.get('https://demoqa.com/links')
driver.maximize_window()

driver.find_element_by_link_text('Home').click()
