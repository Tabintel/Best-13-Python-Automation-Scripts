from pyunitsetup import PyUnitTestSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the website with the modal demo
    setup.driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-modal-demo/")

    # Click on the button to open the modal
    open_modal_button = WebDriverWait(setup.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Launch demo modal')]"))
    )
    open_modal_button.click()

    # Wait for the modal to be visible
    modal = WebDriverWait(setup.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "myModal"))
    )

    # Find and print the modal title
    modal_title = modal.find_element(By.XPATH, "//div[@class='modal-header']/h4")
    print("Modal Title:", modal_title.text)

    # Close the modal by clicking the close button
    close_button = modal.find_element(By.XPATH, "//button[@class='close']")
    close_button.click()

    print("Modal handling successful.")

except Exception as e:
    print("Error occurred while handling modal:", e)

finally:
    # Close the browser
    setup.tearDown()
