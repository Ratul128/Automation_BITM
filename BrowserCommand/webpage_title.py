import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def title():
    driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))

    driver.maximize_window()
    driver.get("https://www.google.com/")
    print(driver.title)
    time.sleep(5)
    driver.quit()

title()