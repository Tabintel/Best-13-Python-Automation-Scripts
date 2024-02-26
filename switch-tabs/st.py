import time
from selenium import webdriver

# Initialize WebDriver with the Edge browser
driver = webdriver.Edge()

# Open the first website in the main tab
driver.get("https://ecommerce-playground.lambdatest.io/")

# Wait for the website to load completely
time.sleep(3)

# Open a new tab
driver.execute_script("window.open('about:blank', '_blank');")

# Wait for a few seconds to let the new tab open
time.sleep(2)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Navigate to the second website
driver.get("https://scrapingclub.com/exercise/list_infinite_scroll/")

# Wait for the website to load completely
time.sleep(3)

# Switch back to the main tab
driver.switch_to.window(driver.window_handles[0])

# Open another new tab
driver.execute_script("window.open('about:blank', '_blank');")

# Wait for a few seconds to let the new tab open
time.sleep(2)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Navigate to the third website
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")

# Wait for the website to load completely
time.sleep(3)

# Switch back to the main tab
driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()
