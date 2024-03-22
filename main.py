import time
from selenium_ultra import Driver

url = input("Enter the URL: ")

driver = Driver()
driver.get(url)
time.sleep(2)
