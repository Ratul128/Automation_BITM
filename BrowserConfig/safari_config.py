from selenium import webdriver

def safari_launch():
    # Initialize the Safari WebDriver
    driver = webdriver.Safari()

    # Open a website
    driver.get("https://www.google.com")

    # Print the page title
    print("Page title is:", driver.title)

    # Close the browser
    driver.quit()

# Call the function
safari_launch()
