import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def webpage_title():
    fDriver=webdriver.Firefox(service = Service(GeckoDriverManager().install()))
    time.sleep(2)

    fDriver.maximize_window()
    time.sleep(2)
    fDriver.set_window_size (360 , 740)
    time.sleep(2)
    #fDriver.set_window_position(100,10)
    '''abc=fDriver.get_window_position()
    print(abc)
    time.sleep(2)'''
    xyz=fDriver.get_window_size()
    print(xyz)
    fDriver.get("https://www.google.com/")
    time.sleep(5)

    fDriver.quit()

webpage_title()
