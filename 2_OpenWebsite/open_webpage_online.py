from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def open_online_webpage():
    driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))

    driver.get("https://www.google.com/")
    driver.close()

open_online_webpage()
