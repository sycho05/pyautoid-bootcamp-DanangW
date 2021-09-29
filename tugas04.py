from selenium import webdriver

data = [["ban","ban@ban.com","disini","disana"]]
driver = webdriver.Chrome(executable_path='C:\chrome_driver\chromedriver.exe')
driver.get('https://demoqa.com/text-box')
driver.maximize_window()

for loop in data:
    driver.find_element_by_id('userName').send_keys(loop[0])
    driver.find_element_by_id('userEmail').send_keys(loop[1])
    driver.find_element_by_id('currentAddress').send_keys(loop[2])
    driver.find_element_by_id('permanentAddress').send_keys(loop[3])

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element_by_id("submit").click()

def test_ber4():
    name = driver.find_element_by_id('name').text
    email = driver.find_element_by_id('email').text
    caddress= driver.find_element_by_css_selector('.border > #currentAddress').text
    paddress= driver.find_element_by_css_selector('.border > #permanentAddress').text
    
    assert name =="Name:ban"
    assert email =="Email:ban@ban.com"
    assert caddress =="Current Address :disini"
    assert paddress =="Permananet Address :disana"
    
def test_nama():
    name = driver.find_element_by_id('name').text
    assert name =="Name:ban"
    
def test_email():
    email = driver.find_element_by_id('email').text
    assert email =="Email:ban@ban.com"
    
def test_caddress():
    caddress= driver.find_element_by_css_selector('.border > #currentAddress').text
    assert caddress =="Current Address :disini"
    
def test_paddress():
    paddress= driver.find_element_by_css_selector('.border > #permanentAddress').text
    assert paddress =="Permananet Address :disaa"
    

