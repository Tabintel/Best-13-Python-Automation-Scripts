from pyunitsetup import PyUnitTestSetup
from selenium import webdriver

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the first website 
    setup.driver.get("https://ecommerce-playground.lambdatest.io/")

    # Get all cookies
    cookies = setup.driver.get_cookies()
    print("Initial cookies:", cookies)

    # Add a new cookie
    new_cookie = {'name': 'example_cookie', 'value': '1234567890'}
    setup.driver.add_cookie(new_cookie)

    # Get updated cookies
    updated_cookies = setup.driver.get_cookies()
    print("Updated cookies:", updated_cookies)

    # Delete the added cookie
    setup.driver.delete_cookie('example_cookie')

    # Get final cookies
    final_cookies = setup.driver.get_cookies()
    print("Final cookies:", final_cookies)

    # Open the second website
    setup.driver.get("https://scrapingclub.com/exercise/list_infinite_scroll/")

    # Open the third website
    setup.driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")

except Exception as e:
    print("Error occurred:", e)

finally:
    # Close the browser
    setup.tearDown()
