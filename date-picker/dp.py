from pyunitsetup import PyUnitTestSetup
from selenium.webdriver.common.by import By
from datetime import datetime

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the website with the date picker
    setup.driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")

    # Find the date input field
    date_input = setup.driver.find_element(By.XPATH, "//input[@id='sandbox-container1']/input")

    # Clear any existing date
    date_input.clear()

    # Send keys to the date input field to set a new date
    date_input.send_keys("02/15/2024")

    # Press Enter key to close the date picker
    date_input.send_keys(Keys.ENTER)

    # Get the selected date from the input field
    selected_date = date_input.get_attribute("value")

    # Convert the selected date string to a datetime object
    selected_date_obj = datetime.strptime(selected_date, "%m/%d/%Y")

    # Compare the input and output dates
    expected_date = datetime(2024, 2, 15)
    if selected_date_obj == expected_date:
        print("Date selected successfully.")
    else:
        print("Error: Selected date does not match expected date.")

except Exception as e:
    print("Error occurred while selecting date:", e)

finally:
    # Close the browser
    setup.tearDown()
