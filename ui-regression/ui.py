from pyunitsetup import PyUnitTestSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Maximize the browser window
    setup.driver.maximize_window()

    # Open the specified URL
    setup.driver.get("https://www.lambdatest.com/smart-visual-ui-testing")

    # Wait for the main heading to be visible
    main_heading = WebDriverWait(setup.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Smart Visual UI Testing')]"))
    )
    assert main_heading.is_displayed(), "Main heading 'Smart Visual UI Testing' not found"

    # Wait for the input field to be visible
    input_field = WebDriverWait(setup.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "search_input"))
    )
    assert input_field.is_displayed(), "Input field not found"

    # Wait for the search button to be visible
    search_button = WebDriverWait(setup.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary']"))
    )
    assert search_button.is_displayed(), "Search button not found"

    # Wait for the navigation menu to be visible
    navigation_menu = WebDriverWait(setup.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "primary_navbar"))
    )
    assert navigation_menu.is_displayed(), "Navigation menu not found"

    # Wait for the footer to be visible
    footer = WebDriverWait(setup.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "footer"))
    )
    assert footer.is_displayed(), "Footer not found"

    print("All UI elements verified successfully.")

except Exception as e:
    print(f"UI regression test failed: {e}")

finally:
    # Close the browser
    setup.tearDown()
