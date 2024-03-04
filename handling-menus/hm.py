from pyunitsetup import PyUnitTestSetup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the website with the menu to be handled
    setup.driver.get("https://ecommerce-playground.lambdatest.io/")

    # Locate the menu element
    menu_element = setup.driver.find_element(By.XPATH, "//span[contains(text(), 'Categories')]")

    # Hover over the menu element to reveal the dropdown
    ActionChains(setup.driver).move_to_element(menu_element).perform()

    # Wait for the dropdown to be visible
    submenu_element = setup.driver.find_element(By.XPATH, "//a[contains(text(), 'Clothing')]")
    submenu_element.click()

    print("Menu handling successful.")

except Exception as e:
    print("Error occurred while handling menus:", e)

finally:
    # Close the browser
    setup.tearDown()
