import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Guru99.Login import guru99_login

def add_customer_valid():
   guru99_login.login_valid()

add_customer_valid()

#add customer practice