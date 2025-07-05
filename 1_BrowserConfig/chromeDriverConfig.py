
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def chrome_launch():
    cdriver=webdriver.Chrome(service = Service(ChromeDriverManager().install()))

chrome_launch()