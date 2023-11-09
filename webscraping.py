import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://devmountain.com/blog/20-top-programming-languages-2020/'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific elements from the webpage
# For example, to find all <a> (anchor) tags with a specific class
specific_elements = soup.find_all('a', class_='specific-class')

# Print or process the extracted data
for element in specific_elements:
    print(element.text)
    # Or perform other operations with the extracted data