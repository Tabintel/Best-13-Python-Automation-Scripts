from selenium import webdriver
from selenium.webdriver.common.alert import Alert

# Initialize the WebDriver with Edge browser
driver = webdriver.Edge()

# Open the website with pop-ups/alerts
driver.get("https://ecommerce-playground.lambdatest.io/")

try:
    # Click on a button that triggers a pop-up
    driver.find_element_by_xpath("//button[contains(text(),'Show Alert')]").click()
    
    # Switch to the alert
    alert = Alert(driver)
    
    # Get the text from the alert
    alert_text = alert.text
    print("Alert text:", alert_text)
    
    # Accept the alert
    alert.accept()
    
    print("Alert accepted successfully.")
    
except Exception as e:
    print("Error occurred while handling alert:", e)

# Close the browser
driver.quit()
