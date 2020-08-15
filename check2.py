from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get('https://mycompany.hyundaicard.com/cm/mn/CMMN1001.do?_method=m')

elem = driver.find_element_by_name("id")
elem.send_keys('kuksan88')

elem = driver.find_element_by_name("pw")
elem.send_keys('tmffoa12#$')
elem.send_keys(Keys.RETURN)

