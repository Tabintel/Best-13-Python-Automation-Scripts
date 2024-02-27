from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver with Edge browser
driver = webdriver.Edge()

# Open the website with the iframe demo
driver.get("https://www.lambdatest.com/selenium-playground/iframe-demo/")

try:
    # Switch to the iframe by name
    iframe_name = "framename"
    driver.switch_to.frame(iframe_name)

    # Perform actions inside the iframe
    # For example, you can interact with elements inside the iframe:
    iframe_heading = driver.find_element(By.XPATH, "//h2[contains(text(), 'This is inside an iframe')]")
    print("Content inside the iframe:", iframe_heading.text)

    # Switch back to the main content
    driver.switch_to.default_content()

    print("iFrame handling successful.")

except Exception as e:
    print("Error occurred while handling iFrame:", e)

# Close the browser
driver.quit()
