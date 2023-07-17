from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://beauty.hotpepper.jp/svcSA/macAD/salon/')
elements = driver.find_elements(By.CLASS_NAME,"message")

elemnt = elements[1].find_element(By.TAG_NAME, 'a')
elemnt.click()