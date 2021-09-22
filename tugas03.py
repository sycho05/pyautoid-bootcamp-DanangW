from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome(executable_path='C:\chrome_driver\chromedriver.exe')
driver.maximize_window()

driver.get('https://demoqa.com/alerts')

try:
    driver.find_element_by_id('timerAlertButton').click()
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("time alert berhasil ditemukan")
except TimeoutException:
    print("time alert tidak berhasil ditemukan")
    
driver.close()