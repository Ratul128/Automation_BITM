'''from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

class Guru_login:
    def __init__(self,firefox_driver):
        self.driver=firefox_driver

    def login_valid (self) :
        self.driver.maximize_window ()
        time.sleep ( 1 )

        self.driver.get ( "https://demo.guru99.com/V4/" )
        time.sleep ( 1 )
        self.driver.find_element ( By.NAME , "uid" ).send_keys ( "mngr627132" )
        time.sleep ( 1 )
        self.driver.find_element ( By.NAME , "password" ).send_keys ( "marUvYm" )
        time.sleep ( 1 )
        self.driver.find_element ( By.NAME , "btnLogin" ).click ( )
        time.sleep ( 2 )

        self.driver.quit()

    def login_invalid (self) :
        self.driver.maximize_window ()
        time.sleep ( 1 )

        self.driver.get ( "https://demo.guru99.com/V4/" )
        time.sleep ( 1 )
        self.driver.find_element ( By.NAME , "uid" ).send_keys ( "mngr627132000" )
        time.sleep ( 1 )
        self.driver.find_element ( By.NAME , "password" ).send_keys ( "marUvYm000" )
        time.sleep ( 1 )
        self.driver.find_element ( By.NAME , "btnLogin" ).click ( )
        time.sleep ( 2 )




obj_class = Guru_login(webdriver.Firefox(service=Service(GeckoDriverManager().install())))

obj_class.login_valid()
obj_class.login_invalid()'''
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

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

    def close_browser(self):
        self.driver.quit()

if __name__=="__main__":
    guru = GuruLogin ()
    guru.login("mngr627132", "marUvYm")
    time.sleep(2)
    guru.login("euwtyuwyr","ewiur")
    time.sleep(3)
    guru.close_browser()

    '''username=input("Enter the username: ")
    password=input("Enter the pasword: ")
    guru.login(username,password)'''
