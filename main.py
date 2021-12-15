import os
from selenium import webdriver

driver = webdriver.Firefox()

os.environ["PATH"] += r"/usr/bin/geckodriver"
driver.get("https://www.facebook.com")
driver.implicitly_wait(30)
one = driver.find_element_by_id("email").send_keys("0797373033")
two = driver.find_element_by_id("pass").send_keys("hartabalin")
# three = driver.find_element_by_id("u_0_h_O2").click()
three = driver.find_element_by_xpath("// button[contains(text(),\'Log In')]").click()
# one.click()