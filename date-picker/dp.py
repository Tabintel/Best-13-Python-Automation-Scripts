from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver with Edge browser
driver = webdriver.Edge()

# Open the website with the date picker
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")

try:
    # Find the date input field
    date_input = driver.find_element(By.XPATH, "//input[@id='sandbox-container1']/input")

    # Clear any existing date
    date_input.clear()

    # Send keys to the date input field to set a new date
    date_input.send_keys("02/15/2024")

    # Press Enter key to close the date picker
    date_input.send_keys(Keys.ENTER)

    print("Date selected successfully.")

except Exception as e:
    print("Error occurred while selecting date:", e)

# Close the browser
driver.quit()
