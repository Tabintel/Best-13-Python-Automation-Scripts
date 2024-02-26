from selenium import webdriver

# Initialize WebDriver with the Edge browser
driver = webdriver.Edge()

# Open the first website 
driver.get("https://ecommerce-playground.lambdatest.io/")

# Get all cookies
cookies = driver.get_cookies()
print("Initial cookies:", cookies)

# Add a new cookie
new_cookie = {'name': 'example_cookie', 'value': '1234567890'}
driver.add_cookie(new_cookie)

# Get updated cookies
updated_cookies = driver.get_cookies()
print("Updated cookies:", updated_cookies)

# Delete the added cookie
driver.delete_cookie('example_cookie')

# Get final cookies
final_cookies = driver.get_cookies()
print("Final cookies:", final_cookies)

# Open the second website
driver.get("https://scrapingclub.com/exercise/list_infinite_scroll/")

# Open the third website
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")

# Close the browser
driver.quit()
