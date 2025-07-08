from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def webpage_title():
    fDriver=webdriver.Firefox(service = Service(GeckoDriverManager().install()))
    fDriver.maximize_window()
    fDriver.get("https://www.google.com/")
    url=fDriver.current_url
    print(url)

    fDriver.quit()

webpage_title()
