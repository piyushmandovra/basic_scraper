import scrapy

class GenericSpider(scrapy.Spider):
    name = "generic_spider"

    def start_requests(self):
        urls = [
            # Add the URLs of the websites you want to scrape here
            'https://openai.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Define the data extraction logic here
        data = {
            'url': response.url,
            'title': response.css('title::text').get(),
            'content': response.css('p::text').getall(),
        }
        yield data
