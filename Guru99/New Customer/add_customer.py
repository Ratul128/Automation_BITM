from Guru99.User_login.login_page import GuruLogin
from selenium.webdriver.common.by import By
import time
import random


class ValidCustomer :

    def add_customer_valid (self) :
        guru2 = GuruLogin ( )
        driver = guru2.login ( "mngr629732" , "ysUsutu" )
        time.sleep ( 3 )

        new_customer = driver.find_element ( By.LINK_TEXT , "New Customer" )
        new_customer.click ( )
        time.sleep ( 2 )

        customer_name = driver.find_element ( By.NAME , "name" )
        customer_name.send_keys ( "ratul" )
        time.sleep ( 1 )

        femail_CSS = ('.layout > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > '
                      'tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > input:nth-child(2)')
        gender_Female = driver.find_element ( By.CSS_SELECTOR , femail_CSS )
        gender_Female.click ( )
        time.sleep ( 1 )

        dateTime = driver.find_element ( By.NAME , 'dob' )
        dateTime.send_keys ( '2025-05-02' )
        time.sleep ( 1 )

        adrs = driver.find_element ( By.NAME , "addr" )
        adrs.send_keys ( "Dhaka" )
        time.sleep ( 1 )

        city = driver.find_element ( By.NAME , "city" )
        city.send_keys ( "Kishoreganj" )
        time.sleep ( 1 )

        state = driver.find_element ( By.NAME , "state" )
        state.send_keys ( "Hossainpur" )
        time.sleep ( 1 )

        pin = driver.find_element ( By.NAME , "pinno" )
        pin.send_keys ( "123456" )
        time.sleep ( 1 )

        mobile = driver.find_element ( By.NAME , "telephoneno" )
        mobile.send_keys ( "01686557297" )
        time.sleep ( 1 )

        randInt = random.randint ( 100 , 200 )
        randEmail = f"ratul{randInt}@gmail.com"
        email = driver.find_element ( By.NAME , "emailid" )
        email.send_keys ( randEmail )
        time.sleep ( 1 )

        pswrd = driver.find_element ( By.NAME , "password" )
        pswrd.send_keys ( "ratul1234" )
        time.sleep ( 1 )

        submit_button = driver.find_element ( By.NAME , "sub" )
        submit_button.click ( )
        time.sleep ( 2 )

        driver.quit ( )

    def customer_name_testCase(self) :
        guru2 = GuruLogin ( )
        driver = guru2.login ( "mngr629732" , "ysUsutu" )
        time.sleep(3)

        new_customer = driver.find_element ( By.LINK_TEXT , "New Customer" )
        new_customer.click ( )
        time.sleep(2)

        #customer name blank test case
        customer_name = driver.find_element ( By.NAME,"name" )
        customer_name.send_keys("")
        time.sleep(1)

        femail_CSS = ('.layout > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > '
                      'tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > input:nth-child(2)')
        gender_Female = driver.find_element ( By.CSS_SELECTOR , femail_CSS )
        gender_Female.click()
        time.sleep ( 1 )

        customerName_Blank_error_message_actual = driver.find_element ( By.ID , "message" ).text
        #print ( customerName_Blank_error_message_actual )

        customerName_Blank_error_message_expected = "Customer name must not be blank1"

        try :
            assert customerName_Blank_error_message_expected == customerName_Blank_error_message_actual
            print("cutomer Name blank issue found")

        except :
            print ("assertion error:customer name blank issue")

        time.sleep(2)

        #1st character space test case
        customer_name.clear()
        customer_name = driver.find_element ( By.NAME , "name" )
        customer_name.send_keys (" ratul")
        time.sleep (1)

        customerName_1stCh_Space_error_message_actual = driver.find_element ( By.ID , "message" ).text
        #print ( customerName_1stCh_Space_error_message_actual )

        customerName_1stCh_space_error_message_expected = "First character can not have space1"

        try :
            assert customerName_1stCh_space_error_message_expected == customerName_1stCh_Space_error_message_actual
            print("1st character space issue Found")

        except :
            print ( "assertion error:First character can not have space" )

        time.sleep (3)

        #number on cutomer name test case
        customer_name.clear()
        time.sleep(1)
        #customer_name = driver.find_element ( By.NAME , "name" )
        customer_name.send_keys ("01686")
        time.sleep(1)

        number_on_Cname_error_message_actual=driver.find_element(By.ID,"message").text
        #print(number_on_Cname_error_message_actual)

        number_on_Cname_error_message_expected="Numbers are not allowed1"

        try:
            assert number_on_Cname_error_message_expected==number_on_Cname_error_message_actual
            print("Number on customer name issue found")
        except:
            print("AssertionError:Numbers are not allowed")
            #print("nothing")
        driver.quit ( )


if __name__ == "__main__" :
    validCustomer = ValidCustomer ( )
    #validCustomer.add_customer_valid()
    validCustomer.customer_name_testCase()
