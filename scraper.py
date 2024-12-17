from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920,1920")

driver = webdriver.Chrome(options=chrome_options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

driver.get("https://www.dhl.com/cz-cs/home/tracking/tracking-global-forwarding.html")
driver.get_screenshot_as_file('s1.png')
inputElement = driver.find_element(by=By.ID, value='c-tracking--input')
inputElement.send_keys('12345')
driver.get_screenshot_as_file('s2.png')
inputElement.submit() 
time.sleep(5)
driver.get_screenshot_as_file('s3.png')

driver.quit()
