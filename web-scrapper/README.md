# Quote Scraper

A small Python script that scrapes quotes from [quotes.toscrape.com](https://quotes.toscrape.com) and saves them to a CSV file.

## What it does

- Fetches the homepage of `quotes.toscrape.com`
- Extracts each quote's **text**, **author**, and **tags**
- Prints each quote to the console
- Writes all quotes to `quotes.csv` in the current directory

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

```bash
python scrape_quotes_simple.py
```

## Output

A file named `quotes.csv` is created with three columns:

| Quote | Author | Tags |
|-------|--------|------|
| "The world as we have created it is a process of our thinking..." | Albert Einstein | change, deep-thoughts, thinking, world |

## Error handling

The script is wrapped in a `try/except` block that handles:

- **Network errors** (`requests.exceptions.RequestException`) — e.g. no internet connection, timeout, bad status code
- **File write errors** (`OSError`) — e.g. no write permission, disk full
- **Malformed quote blocks** (`AttributeError`) — individual quotes missing expected fields are skipped, and the rest still get processed
- **Any other unexpected error** — caught as a final safety net so the script never crashes with a raw traceback