import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def set_browser_size():
    driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
    driver.set_window_size(768,1024)

    driver.get("https://demo.opencart.com/index.php")
    time.sleep(4)
    driver.quit()

set_browser_size()