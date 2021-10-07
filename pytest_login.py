from selenium import webdriver
import pytest
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get('https://zateens.com/my-account-2/')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
# send_keys('ximefo@musiccode.me')
def test_login_success(setup): #testcase 001
    setup.find_element_by_id('username').send_keys('jajang@mail.com')
    setup.find_element_by_id('password').send_keys('mail123123_')
    setup.find_element_by_name('login').click()
    Badge = setup.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/main/article/div/div/div/p[1]/strong[1]')[0].text
    assert Badge == 'jajang'
    
Accounts = [('jajang@mail.com','mail123123_'),
            ('jajang@smail.com',''),
            ('','smail123123_')]

@pytest.mark.parametrize('a,b', Accounts)
def test_login_unsuccess(setup,a,b): #testcase 002,003,004
    setup.find_element_by_id('username').send_keys(a)
    setup.find_element_by_id('password').send_keys(b)
    setup.find_element_by_name('login').click()
    Alert = setup.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/main/article/div/div/nav/ul/li[6]/a').is_displayed()
    assert Alert == True
