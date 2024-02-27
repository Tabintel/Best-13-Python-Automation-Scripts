from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver with Edge browser
driver = webdriver.Edge()

# Open the website with the menu to be handled
driver.get("https://ecommerce-playground.lambdatest.io/")

try:
    # Locate the menu element
    menu_element = driver.find_element(By.XPATH, "//span[contains(text(), 'Categories')]")

    # Hover over the menu element to reveal the dropdown
    ActionChains(driver).move_to_element(menu_element).perform()

    # Wait for the dropdown to be visible
    submenu_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Clothing')]")
    submenu_element.click()

    print("Menu handling successful.")

except Exception as e:
    print("Error occurred while handling menus:", e)

# Close the browser
driver.quit()
