from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# Specify the path to the Edge WebDriver executable
edge_driver_path = r"C:\Users\USER\Downloads\apps\edgedriver_win64\msedgedriver.exe"

# Create a service object
service = Service(edge_driver_path)

# Initialize WebDriver with the Edge browser and the service
driver = webdriver.Edge(service=service)

# Maximize the browser window
driver.maximize_window()

# Open the website with dynamic content
driver.get("https://scrapingclub.com/exercise/list_infinite_scroll/")  # Or any other URL with dynamic content

try:
    # Wait for dynamic content to load (e.g., lazy-loaded images)
    # You may need to implement specific wait conditions based on the behavior of the website
    # For example, you can wait for a specific element to be present or visible
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lazyload")))

    # Verify the presence of dynamic content
    dynamic_content = driver.find_elements(By.CLASS_NAME, "lazyload")
    if dynamic_content:
        print("Dynamic content loaded successfully.")
    else:
        print("No dynamic content found.")

except Exception as e:
    print(f"Failed to load dynamic content: {e}")

# Close the browser
driver.quit()
