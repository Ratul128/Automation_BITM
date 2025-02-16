from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

def logIn():
    driver=webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()

    driver.get("https://anzaar.bitcommerz.com/auth/login")
    time.sleep(1)

    email_field=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/form/div[1]/div/input')
    email_field.send_keys('ratulqabbt@gmail.com')
    time.sleep(1)

    pass_field=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/form/div[2]/div/div/div[2]/input')
    pass_field.send_keys('ratul1234')
    time.sleep(1)

    clickOn_logIn_button=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/form/button')
    clickOn_logIn_button.click()

    time.sleep(3)
    driver.quit()

logIn()

