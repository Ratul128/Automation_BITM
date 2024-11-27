from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
def firefox_launch () :
    # Path to GeckoDriver
    gecko_path = "/Users/nurulamin/Desktop/PythonLearning/geckodriver"

    # Create a Service object for GeckoDriver
    fDriver_path = Service(gecko_path)

    # Initialize the Firefox driver
    driver = webdriver.Firefox(service = fDriver_path)

    driver.get("https://www.google.com/")

    # to close to current window
    driver.close()

firefox_launch()
