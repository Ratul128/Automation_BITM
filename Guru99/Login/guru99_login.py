import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def login_valid():
    driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()

    driver.get("https://demo.guru99.com/Agile_Project/Agi_V1/")
    user_id=driver.find_element(By.NAME,"uid")
    user_id.send_keys("mngr603789")

    password=driver.find_element(By.NAME,"password")
    password.send_keys("qydAbag")

    click_login=driver.find_element(By.NAME,"btnLogin")
    click_login.click()

    time.sleep(3)
    driver.quit()

login_valid()