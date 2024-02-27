from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver with Edge browser
driver = webdriver.Edge()

# Open the website with the table pagination demo
driver.get("https://www.lambdatest.com/selenium-playground/table-pagination-demo")

try:
    # Wait for the table to load
    time.sleep(3)

    # Find all table rows
    rows = driver.find_elements(By.XPATH, "//table[@id='myTable']/tbody/tr")

    # Print the content of each row
    for row in rows:
        print(row.text)

    print("Web table handled successfully.")

except Exception as e:
    print("Error occurred while handling web table:", e)

# Close the browser
driver.quit()
