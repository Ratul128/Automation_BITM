from Guru99.User_login.login_page import GuruLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ValidCustomer:

    def __init__(self):
        self.username = "mngr627132"
        self.password = "marUvYm"
        self.wait_time = 10
        self.driver = None

    def wait_and_find(self, by, value):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((by, value))
        )

    def fill_customer_form(self):
        # Open New Customer Page
        new_customer = self.wait_and_find(By.LINK_TEXT, "New Customer")
        new_customer.click()

        # Fill form
        self.wait_and_find(By.NAME, "name").send_keys("ratul")

        gender_female_css = (
            '.layout > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > '
            'tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > input:nth-child(2)'
        )
        self.driver.find_element(By.CSS_SELECTOR, gender_female_css).click()

        self.driver.find_element(By.NAME, 'dob').send_keys('2025-05-02')
        self.driver.find_element(By.NAME, 'addr').send_keys('Dhaka')
        self.driver.find_element(By.NAME, 'city').send_keys('Kishoreganj')
        self.driver.find_element(By.NAME, 'state').send_keys('Hossainpur')
        self.driver.find_element(By.NAME, 'pinno').send_keys('123456')
        self.driver.find_element(By.NAME, 'telephoneno').send_keys('01686557297')
        self.driver.find_element(By.NAME, 'emailid').send_keys('ratul11@gmail.com')
        self.driver.find_element(By.NAME, 'password').send_keys('ratul1234')

        self.driver.find_element(By.NAME, 'sub').click()

    def add_valid_customer(self):
        try:
            guru_login = GuruLogin()
            self.driver = guru_login.login(self.username, self.password)
            self.fill_customer_form()
        finally:
            if self.driver:
                self.driver.quit()


if __name__ == "__main__":
    valid_customer = ValidCustomer()
    valid_customer.add_valid_customer()
