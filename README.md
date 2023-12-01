# amazon-python-scrapy-scraper
Python Scrapy spiders that scrape product data and reviews from [Amazon.com](https://www.amazon.com/). 

 `amazon_search_product` |  Crawls Amazon product search pages for a given list of keywords, then scrapes each individual product page.

## ScrapeOps Proxy
This Amazon spider uses [ScrapeOps Proxy](https://scrapeops.io/proxy-aggregator/) as the proxy solution. ScrapeOps has a free plan that allows you to make up to 1,000 requests per month which makes it ideal for the development phase, but can be easily scaled up to millions of pages per month if needs be.

You can [sign up for a free API key here](https://scrapeops.io/app/register/main).

To use the ScrapeOps Proxy you need to first install the proxy middleware:

```python

pip install scrapeops-scrapy-proxy-sdk

```

Then activate the ScrapeOps Proxy by adding your API key to the `SCRAPEOPS_API_KEY` in the ``settings.py`` file.

```python

SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

```

## Running The Scrapers
Make sure Scrapy and the ScrapeOps Monitor is installed:

```

pip install scrapy scrapeops-scrapy

```

To run the Amazon spiders you should first set the search query parameters you want to search by updating the `keyword_list` list in the spiders:

```python

def start_requests(self):
    keyword_list = ['ipad']
    for keyword in keyword_list:
        amazon_search_url = f'https://www.amazon.com/s?k={keyword}&page=1'
        yield scrapy.Request(url=amazon_search_url, callback=self.parse_search_results, meta={'keyword': keyword, 'page': 1})

```

Then to run the spider, enter one of the following command:

```

scrapy crawl amazon_search_product 

```
** To terminate the spider, press CTRL+C


### Storing Data
The spiders are set to save the scraped data into a CSV file and store it in a data folder using [Scrapy's Feed Export functionality](https://docs.scrapy.org/en/latest/topics/feed-exports.html).

```python

custom_settings = {
        'FEEDS': { 'data/%(name)s_%(time)s.csv': { 'format': 'csv',}}
        }

```

If you would like to save your CSV files to an Excel file, you must: 

1. Locate the folder on your machine 
2. Open the data folder containing the CSV Files
3. Click the "Data" tab on Excel 
4. Click "Import from CSV" 
Video Instructions: https://www.youtube.com/watch?v=ebnNy5yEkvc


** under 6 years + blurb