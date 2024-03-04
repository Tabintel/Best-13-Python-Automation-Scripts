from pyunitsetup import PyUnitTestSetup
from selenium.webdriver.common.by import By

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the website with the iframe demo
    setup.driver.get("https://www.lambdatest.com/selenium-playground/iframe-demo/")

    # Switch to the iframe by name
    iframe_name = "framename"
    setup.driver.switch_to.frame(iframe_name)

    # Perform actions inside the iframe
    # For example, you can interact with elements inside the iframe:
    iframe_heading = setup.driver.find_element(By.XPATH, "//h2[contains(text(), 'This is inside an iframe')]")
    print("Content inside the iframe:", iframe_heading.text)

    # Switch back to the main content
    setup.driver.switch_to.default_content()

    print("iFrame handling successful.")

except Exception as e:
    print("Error occurred while handling iFrame:", e)

finally:
    # Close the browser
    setup.tearDown()
