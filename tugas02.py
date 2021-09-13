from selenium import webdriver
import time

data = [
    ["ban","nang","banang@danang.com","21","10000","PYAUTO"],
    ["can","nang","canang@danang.com","22","20000","PYAUTO2"],
    ["dan","nang","danang@danang.com","23","30000","PYAUTO3"]
]

driver = webdriver.Chrome(executable_path='C:\chrome_driver\chromedriver.exe')
driver.get('https://demoqa.com/webtables')
driver.maximize_window()

for loop in data:
    driver.find_element_by_id('addNewRecordButton').click()
    driver.find_element_by_id('firstName').send_keys(loop[0])
    driver.find_element_by_id('lastName').send_keys(loop[1])
    driver.find_element_by_id('userEmail').send_keys(loop[2])
    driver.find_element_by_id('age').send_keys(loop[3])
    driver.find_element_by_id('salary').send_keys(loop[4])
    driver.find_element_by_id('department').send_keys(loop[5])
    driver.find_element_by_id('submit').click()
    
time.sleep(5)
driver.close()
    