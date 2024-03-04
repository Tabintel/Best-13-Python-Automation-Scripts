import time
from pyunitsetup import PyUnitTestSetup

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the first website in the main tab
    setup.driver.get("https://ecommerce-playground.lambdatest.io/")

    # Wait for the website to load completely
    time.sleep(3)

    # Open a new tab
    setup.driver.execute_script("window.open('about:blank', '_blank');")

    # Wait for a few seconds to let the new tab open
    time.sleep(2)

    # Switch to the new tab
    setup.driver.switch_to.window(setup.driver.window_handles[1])

    # Navigate to the second website
    setup.driver.get("https://scrapingclub.com/exercise/list_infinite_scroll/")

    # Wait for the website to load completely
    time.sleep(3)

    # Switch back to the main tab
    setup.driver.switch_to.window(setup.driver.window_handles[0])

    # Open another new tab
    setup.driver.execute_script("window.open('about:blank', '_blank');")

    # Wait for a few seconds to let the new tab open
    time.sleep(2)

    # Switch to the new tab
    setup.driver.switch_to.window(setup.driver.window_handles[1])

    # Navigate to the third website
    setup.driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")

    # Wait for the website to load completely
    time.sleep(3)

    # Switch back to the main tab
    setup.driver.switch_to.window(setup.driver.window_handles[0])

    print("Tabs switched successfully.")

except Exception as e:
    print(f"Error occurred while switching tabs: {e}")

finally:
    # Close the browser
    setup.tearDown()
