import csv
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://ecommerce-playground.lambdatest.io/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

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
