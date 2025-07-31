from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


'''def login_valid ( ) :
    driver = webdriver.Firefox ( service = Service ( GeckoDriverManager ( ).install ( ) ) )
    driver.maximize_window ( )
    time.sleep ( 1 )

    driver.get ( "https://demo.guru99.com/V4/" )
    time.sleep ( 1 )
    driver.find_element ( By.NAME , "uid" ).send_keys ( "mngr627132" )
    time.sleep ( 1 )
    driver.find_element ( By.NAME , "password" ).send_keys ( "marUvYm" )
    time.sleep ( 1 )
    driver.find_element ( By.NAME , "btnLogin" ).click ( )
    time.sleep ( 2 )

    driver.quit ( )


if __name__ =="__main__":
    login_valid ( )'''


class GuruLogin:
    def __init__(self):
        self.driver = webdriver.Firefox ( service = Service ( GeckoDriverManager ( ).install ( ) ) )
        self.driver.maximize_window()
        time.sleep(1)

    def login(self,username,password):
        self.driver.get("https://demo.guru99.com/V4/")
        time.sleep(1)
        self.driver.find_element(By.NAME,"uid").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.NAME,"btnLogin").click()

        return self.driver

    def close_browser(self):
        self.driver.quit()

if __name__=="__main__":
    guru = GuruLogin ()
    guru.login("mngr629732", "ysUsutu")
    time.sleep(2)
    '''guru.login("euwtyuwyr","ewiur")
    time.sleep(3)'''
    guru.close_browser()

    '''username=input("Enter the username: ")
    password=input("Enter the pasword: ")
    guru.login(username,password)'''
