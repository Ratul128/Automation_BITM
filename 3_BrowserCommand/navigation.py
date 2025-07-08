from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

def navigation():
    fdriver=webdriver.Firefox(service = Service(GeckoDriverManager().install()))
    time.sleep(3)

    fdriver.maximize_window()
    time.sleep(3)
    fdriver.get("https://anzaarlifestyle.com/")
    time.sleep(3)
    fdriver.get("https://gadgetandgear.com/")
    time.sleep(3)

    fdriver.back()
    time.sleep(3)
    fdriver.forward()
    time.sleep(3)
    fdriver.refresh()
    time.sleep(3)

    fdriver.quit()
navigation()