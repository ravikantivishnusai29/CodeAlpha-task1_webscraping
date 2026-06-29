import requests
from bs4 import BeautifulSoup
import pandas as pd

all_titles = []
all_prices = []
all_ratings = []

# Scrape first 5 pages (100 books)
for page in range(1, 6):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text

        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]

        all_titles.append(title)
        all_prices.append(price)
        all_ratings.append(rating)

# Create DataFrame
df = pd.DataFrame({
    "Title": all_titles,
    "Price": all_prices,
    "Rating": all_ratings
})

# Save to CSV
df.to_csv("books_100_records.csv", index=False)

print("Dataset saved successfully!")

# Display first 5 rows
print(df.head())