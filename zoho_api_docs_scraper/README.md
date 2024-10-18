### Run scrapy

1. Scrape:
   - Go to [zoho_api_docs_scraper](../zoho_api_docs_scraper) directory and run:
    ```bash
    zoho_api_docs_scraper$ scrapy crawl zoho_api_docs -O apis.json
    ```
   - Find the result in apis.json file
2. Shell
```commandline
scrapy shell  https://www.zoho.com/books/api/v3/invoices/#create-an-invoice
```