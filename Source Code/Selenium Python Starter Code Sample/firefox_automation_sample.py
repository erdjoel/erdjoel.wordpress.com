from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

geckodriver = r"C:\Users\ridwan julvianto\AppData\Local\Programs\SeleniumDrivers\geckodriver-v0.19.1-win32\geckodriver.exe"
binary = FirefoxBinary(r"C:\Users\ridwan julvianto\AppData\Local\Programs\Browsers\Mozilla Firefox56.0.2-x86\firefox.exe")
fp = webdriver.FirefoxProfile()

driver = webdriver.Firefox(executable_path=geckodriver, firefox_binary=binary, firefox_profile=fp) #Optional, if not specified, WebDriver will search your path for geckodriver.
#driver = webdriver.Firefox()
driver.get("http://www.python.org")

#assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

#assert "No results found." not in driver.page_source

#driver.quit()