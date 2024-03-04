from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitsetup import PyUnitTestSetup

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

# Open the website with the table pagination demo
setup.driver.get("https://www.lambdatest.com/selenium-playground/table-pagination-demo")

try:
    # Wait for the table to load
    WebDriverWait(setup.driver, 10).until(EC.presence_of_element_located((By.ID, "myTable")))

    # Find all table rows
    rows = setup.driver.find_elements(By.XPATH, "//table[@id='myTable']/tbody/tr")

    # Print the content of each row
    for row in rows:
        print(row.text)

    print("Web table handled successfully.")

except Exception as e:
    print("Error occurred while handling web table:", e)

finally:
    # Close the browser
    setup.tearDown()
