import json
import scrapy
from urllib.parse import urljoin
import re
import json


class AmazonSearchProductSpider(scrapy.Spider):
    name = "amazon_search_product"


    custom_settings = {
        'FEEDS': { 'data/%(name)s_%(time)s.csv': { 'format': 'csv',}}
        }
   
# keyword input. Change to liking. 
    def start_requests(self):
        keyword_list = ['Native American Heritage month books']
        for keyword in keyword_list:
            amazon_search_url = f'https://www.amazon.com/s?k={keyword}&page=1'
            yield scrapy.Request(url=amazon_search_url, callback=self.discover_product_urls, meta={'keyword': keyword, 'page': 1})


    def discover_product_urls(self, response):
        page = response.meta['page']
        keyword = response.meta['keyword']


        ## Discover Product URLs
        search_products = response.css("div.s-result-item[data-component-type=s-search-result]")
        for product in search_products:
            relative_url = product.css("h2>a::attr(href)").get()
            product_url = urljoin('https://www.amazon.com/', relative_url).split("?")[0]
            yield scrapy.Request(url=product_url, callback=self.parse_product_data, meta={'keyword': keyword, 'page': 1})
           




    def parse_product_data(self, response):
       
        stars = response.css("i[data-hook=average-star-rating] ::text").get("").strip()
       
        stars_float = float(re.search(r'([\d.]+)', stars).group()) if re.search(r'([\d.]+)', stars) else 0.0
        reviews_text = response.css("span#acrCustomerReviewText.a-size-base::text").get()
        num_reviews = int(re.sub(r'[^\d]', '', reviews_text)) if reviews_text else 0
       
       
       
        if stars_float >= 4.5 and num_reviews >= 100:
            image_data = json.loads(re.findall(r"colorImages':.*'initial':\s*(\[.+?\])},\n", response.text)[0])
            main_image = None
           
            for image in image_data:
                if "variant" in image and image["variant"] == "MAIN":
                    main_image = image.get("large", image.get("hiRes"))
                    break
            author_name = response.css("span.author a.a-link-normal::text").getall()
            book_description = response.css("div#bookDescription_feature_div div.a-expander-content span::text").getall()
            book_description = ' '.join(book_description).strip()


            
            reading_age = response.css("div.a-section.a-spacing-none.a-text-center.rpi-attribute-value span::text").get()     
            if not reading_age:
                reading_age = response.css("div.a-section.a-spacing-none.a-text-center.rpi-attribute-value [data-a-modal*='Customer Recommended Reading Age'] span::text").get()

           
            yield {
                "Book Name": response.css("#productTitle::text").get("").strip(),
                "Author Name": author_name,
                "Reading Age": reading_age if reading_age else None,  # Include the reading age (or None if not found)
                "Rating": stars,
                "Number of Reviews": num_reviews,  
                "Book Description": book_description,
                "Image Link": main_image,
                "Amazon Book Link": response.url,
                
            }
    
    
    








