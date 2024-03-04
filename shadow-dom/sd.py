from pyunitsetup import PyUnitTestSetup

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

try:
    # Open the website with Shadow DOM
    setup.driver.get("https://www.lambdatest.com/selenium-playground/shadow-dom")

    # Execute JavaScript to find and print the content of the Shadow DOM element
    shadow_dom_content = setup.driver.execute_script("return document.querySelector('my-app').shadowRoot.querySelector('h3')")
    print("Shadow DOM Content:", shadow_dom_content.text)

    print("Shadow DOM handling successful.")

except Exception as e:
    print("Error occurred while handling Shadow DOM:", e)

finally:
    # Close the browser
    setup.tearDown()
