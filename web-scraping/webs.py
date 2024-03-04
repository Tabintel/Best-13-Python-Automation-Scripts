import csv
import requests
from bs4 import BeautifulSoup
from pyunitsetup import PyUnitTestSetup

# Initialize the PyUnitTestSetup fixture
setup = PyUnitTestSetup()

# URL of the website to scrape
url = "https://ecommerce-playground.lambdatest.io/"

try:
    # Send a GET request to the URL
    response = setup.driver.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(setup.driver.page_source, "html.parser")

    # Find all product containers
    product_links = soup.select('nav.vertical a.nav-link')

    # Define the filename for the CSV file
    filename = "product_categories.csv"

    # Open the CSV file in write mode and create a CSV writer object
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(["Category"])

        # Iterate over each product link and extract product category
        for link in product_links:
            # Extract product category
            category = link.select_one('.title').text.strip()

            # Write product category to the CSV file
            writer.writerow([category])

    print("Product categories have been saved to", filename)

except Exception as e:
    print("Error occurred while scraping:", e)

finally:
    # Close the browser
    setup.tearDown()
