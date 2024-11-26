from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def chrome_launch():
    # Specify the correct path to your ChromeDriver
    cDriver_path = Service("/Users/nurulamin/Desktop/PythonLearning/chromedriver-mac-x64/chromedriver")

    # Initialize the Chrome WebDriver using the Service object
    driver = webdriver.Chrome(service = cDriver_path)

    # Open Google's homepage
    driver.get("https://www.google.com/")
    time.sleep(10)
chrome_launch()



