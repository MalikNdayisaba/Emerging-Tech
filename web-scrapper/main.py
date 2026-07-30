#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://quotes.toscrape.com"
 
 
def main():
    try:
        response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
 
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
 
        with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author", "Tags"])
            for quote in quotes:
                try:
                    text = quote.find("span", class_="text").get_text(strip=True)
                    author = quote.find("small", class_="author").get_text(strip=True)
                    tags = ", ".join(tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag"))
                    writer.writerow([text, author, tags])
                    print(f'"{text}" - {author} ({tags})')
                except AttributeError:
                    print("Skipping a quote block with missing data.")
 
        print("Quotes have been written to quotes.csv")
 
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {URL}: {e}")
    except OSError as e:
        print(f"Failed to write quotes.csv: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
 
 
if __name__ == "__main__":
    main()