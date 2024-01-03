
BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

SCRAPEOPS_API_KEY = '22e5961a-aea5-480e-baf5-2a82df5ba3dc'

SCRAPEOPS_PROXY_ENABLED = True
# SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}

DOWNLOADER_MIDDLEWARES = { 
    ## Proxy Middleware
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1

# ITEM_PIPELINES = {
#    'amazon.pipelines.MysqlDemoPipeline': 300,
# }

