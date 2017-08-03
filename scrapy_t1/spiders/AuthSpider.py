'''
Created on 2017年8月3日

@author: lenovo
'''

import scrapy


class AuthSpider(scrapy.Spider):
    name = "author"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        yield{
              'url':response.url,
        }
        #print(response.url)
        for ft in response.xpath('//div[@class="quote"]'):
            yield {
                'text': ft.xpath('.//span[@class="text"]/text()').extract_first(),
                'author': ft.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': ft.xpath('.//div[@class="tags"]').xpath('.//a/text()').extract(),
            }
        
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)