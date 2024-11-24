from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


def firefox_launch () :
    # Path to GeckoDriver
    gecko_path = "/Users/nurulamin/Desktop/PythonLearning/geckodriver"

    # Create a Service object for GeckoDriver
    fDriver_path = Service(gecko_path)

    # Initialize the Firefox driver
    driver = webdriver.Firefox (service = fDriver_path)

    # Open a website to test
    driver.get("https://www.google.com")

    # Print the title of the webpage
    print ( "Page title is:" , driver.title )

    # Keep the browser open for 5 seconds
    time.sleep(5)

    # Close the browser
    driver.quit()

# Call the function to launch Firefox
firefox_launch()
