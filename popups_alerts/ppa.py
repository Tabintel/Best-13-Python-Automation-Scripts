from pyunitsetup import PyUnitTestSetup
from selenium.webdriver.common.alert import Alert

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the website with pop-ups/alerts
    setup.driver.get("https://ecommerce-playground.lambdatest.io/")

    # Click on a button that triggers a pop-up
    setup.driver.find_element_by_xpath("//button[contains(text(),'Show Alert')]").click()
    
    # Switch to the alert
    alert = Alert(setup.driver)
    
    # Get the text from the alert
    alert_text = alert.text
    print("Alert text:", alert_text)
    
    # Accept the alert
    alert.accept()
    
    print("Alert accepted successfully.")
    
except Exception as e:
    print("Error occurred while handling alert:", e)

finally:
    # Close the browser
    setup.tearDown()
