from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def offline_webpage_launch():
    gecho_path="/Users/nurulamin/Desktop/PythonLearning/geckodriver"
    fDriver_path= Service(gecho_path)
    driver=webdriver.Firefox(service = fDriver_path)

    driver.get("file:///Users/nurulamin/Desktop/PythonLearning/ romanian-baloch627.htm")

    driver.close()

offline_webpage_launch()
