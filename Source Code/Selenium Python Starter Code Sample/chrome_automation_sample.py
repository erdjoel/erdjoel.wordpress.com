from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromedriver = r"C:\Users\ridwan julvianto\AppData\Local\Programs\SeleniumDrivers\chromedriver-v2.33_win32\chromedriver.exe"

options = Options()
#options.add_argument("--start-maximized")
#options.add_argument("--disable-infobars")
#options.add_argument("--disable-extensions")
#options.add_argument(r"--profile-directory='TestProfile' --user-data-dir='C:\Users\ridwan julvianto\AppData\Local\Programs\Browsers\Chrome62.0.3202.62\UserData'");
#options.binary_location = r"C:\Users\ridwan julvianto\AppData\Local\Programs\Browsers\Chrome62.0.3202.62\chrome.exe"
options.binary_location = r"C:\Users\ridwan julvianto\AppData\Local\Programs\Browsers\Chromium\chrome.exe"

#driver = webdriver.Chrome()
#driver = webdriver.Chrome(chromedriver) #Optional, if not specified, WebDriver will search your path for chromedriver.
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver.get("http://www.python.org")

#assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

#assert "No results found." not in driver.page_source

#driver.quit()