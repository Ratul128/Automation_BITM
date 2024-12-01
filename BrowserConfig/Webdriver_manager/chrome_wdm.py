import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def chrome_webdriver_manager():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.maximize_window()
    driver.get("https://www.google.com/")
    time.sleep(5)
    driver.quit()

chrome_webdriver_manager()