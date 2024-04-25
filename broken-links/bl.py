#from pyunitsetup import PyUnitTestSetup
from selenium.webdriver.common.by import By
import requests

# Initialize the PyUnitTestSetup fixture
#setup = PyUnitTestSetup()
setup.setUp()  # Added setUp() method call here

try:
    # Open the specified URL
    setup.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57")

    # Extract all the links on the page
    links = setup.driver.find_elements(By.TAG_NAME, 'a')

    # Iterate through each link and check its status code
    for link in links:
        url = link.get_attribute('href')
        if url:  # Check if the URL is not empty
            try:
                response = requests.head(url)
                if response.status_code != 200:
                    print(f"Broken Link Found: {url} - Status Code: {response.status_code}")
            except requests.exceptions.MissingSchema:
                print(f"Invalid URL: {url} - No scheme supplied.")
            except requests.exceptions.RequestException as e:
                print(f"Error accessing URL: {url} - {e}")

    print("Broken links checked successfully.")

except Exception as e:
    print("Error occurred while checking broken links:", e)

finally:
    # Close the browser
    setup.tearDown()
