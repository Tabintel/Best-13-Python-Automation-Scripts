from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.edge.service import Service

# Specify the path to the Edge WebDriver executable
edge_driver_path = r"C:\Users\USER\Downloads\apps\edgedriver_win64\msedgedriver.exe"

# Create a service object
service = Service(edge_driver_path)

# Start the WebDriver service
service.start()

# Initialize WebDriver with the Edge browser and the service
driver = webdriver.Edge(service=service)

# Maximize the browser window
driver.maximize_window()

# Open the specified URL
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57")

# Extract all the links on the page
links = driver.find_elements(By.TAG_NAME, 'a')

# Iterate through each link and check its status code
for link in links:
    url = link.get_attribute('href')
    if url:  # Check if the URL is not empty
        try:
            response = requests.head(url)
            if response.status_code != 200:
                print(f"Broken Link Found: {url} - Status Code: {response.status_code}")
        except requests.exceptions.MissingSchema:
            print(f"Invalid URL: {url} - No scheme supplied.")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing URL: {url} - {e}")

# Close the browser
driver.quit()
