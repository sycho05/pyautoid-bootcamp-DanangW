from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\chrome_driver\chromedriver.exe')
driver.get('https://demoqa.com/webtables')
driver.maximize_window()

for i in range(3):
    driver.find_element_by_id('addNewRecordButton').click()
    driver.find_element_by_id('firstName').send_keys('Dan'+str(i+1))
    driver.find_element_by_id('lastName').send_keys('nang'+str(i+1))
    driver.find_element_by_id('userEmail').send_keys('Danang'+str(i+1)+'@danang.com')
    driver.find_element_by_id('age').send_keys('22')
    driver.find_element_by_id('salary').send_keys('10000')
    driver.find_element_by_id('department').send_keys('PyAuto'+str(i+1))
    driver.find_element_by_id('submit').click()
    print('Inputan'+str(i+1))
    
time.sleep(5)
driver.close()
    