from pyunitsetup import PyUnitTestSetup
from selenium.webdriver.common.by import By

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the website with dynamic content
    setup.driver.get("https://scrapingclub.com/exercise/list_infinite_scroll/")  # Or any other URL with dynamic content

    # Verify the presence of dynamic content
    dynamic_content = setup.driver.find_elements(By.CLASS_NAME, "lazyload")
    if dynamic_content:
        print("Dynamic content loaded successfully.")
    else:
        print("No dynamic content found.")

except Exception as e:
    print(f"Failed to load dynamic content: {e}")

finally:
    # Close the browser
    setup.tearDown()
