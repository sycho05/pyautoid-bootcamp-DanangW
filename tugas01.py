from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\chrome_driver\chromedriver.exe')
list = ['http://noobtest.id','http://erzaf.com','http://orangsiber.com','http://demoqa.com','https://automatetheboringstuff.com/']
driver.minimize_window()
for url in list:
    driver.get(url)
    print(driver.current_url[8:-1]+" - "+ driver.title)
driver.close()