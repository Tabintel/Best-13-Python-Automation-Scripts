from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to the Edge WebDriver executable
edge_driver_path = r"C:\Users\USER\Downloads\apps\edgedriver_win64\msedgedriver.exe"

# Initialize the Edge WebDriver
driver = webdriver.Edge(executable_path=edge_driver_path)

# Maximize the browser window (optional)
driver.maximize_window()

# Open the URL
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")

try:
    # Find and click on the date picker input field
    date_picker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
    date_picker.click()

    # Clear any existing date in the input field
    date_picker.clear()

    # Enter a new date (e.g., "10/10/2023")
    date_picker.send_keys("10/10/2023")

    # Send ENTER key to confirm the selected date
    date_picker.send_keys(Keys.ENTER)

    # Wait for a while to see the selected date
    time.sleep(2)

    print("Date selected successfully.")

except Exception as e:
    print(f"Error: {e}")

# Close the browser
driver.quit()
