from selenium import webdriver

# Initialize the WebDriver with Edge browser
driver = webdriver.Edge()

# Open the website with Shadow DOM
driver.get("https://www.lambdatest.com/selenium-playground/shadow-dom")

try:
    # Execute JavaScript to find and print the content of the Shadow DOM element
    shadow_dom_content = driver.execute_script("return document.querySelector('my-app').shadowRoot.querySelector('h3')")
    print("Shadow DOM Content:", shadow_dom_content.text)

    print("Shadow DOM handling successful.")

except Exception as e:
    print("Error occurred while handling Shadow DOM:", e)

# Close the browser
driver.quit()
