
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

def navigation():
    driver=webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()

    driver.get("https://gadgetandgear.com/")
    time.sleep(2)
    driver.get("https://anzaarlifestyle.com/")
    time.sleep(2)

    driver.back()
    time.sleep(2)

    driver.forward()
    time.sleep(2)

    driver.refresh()
    time.sleep(2)

    driver.quit()

navigation()

