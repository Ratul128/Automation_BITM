
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def firefox_launch():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    #to config firefox automatically
    driver.maximize_window()
    driver.get("https://www.google.com/")

    driver.close()

firefox_launch()