import requests
from bs4 import BeautifulSoup
import csv

# URL of the practice website
url = 'http://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Open a CSV file to store the scraped data
with open('books_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Availability'])

    # Find all book containers on the page
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        # Extract book title
        title = book.find('h3').find('a')['title']

        # Extract book price
        price = book.find('p', class_='price_color').get_text(strip=True)

        # Extract availability status
        availability = book.find('p', class_='instock availability').get_text(strip=True)

        # Write data to CSV file
        writer.writerow([title, price, availability])

print("Data scraping completed. Check 'books_data.csv' for results.")