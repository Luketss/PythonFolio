import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}

'''import urllib.parse
import scrapy

from scrapy.http import Request

class droficial(scrapy.Spider):
    name = "droficial"

    start_urls = [
        "https://diariooficial.santos.sp.gov.br/edicoes/inicio/download/2016-04-18"
    ]

    def parse(self, response):
        result = response.text()
        save_pdf(result)


    def save_pdf(self, response):
        filename = 'quotes-1.txt'
        with open(filename, 'wb') as f:
            f.write(response.body)

# import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = 'nini'
#     date = '2021-02-12'

#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.css('small.author::text').get(),
#                 'tags': quote.css('div.tags a.tag::text').getall(),
#             }

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             for quote in response.css('div.quote'):
#                 yield {
#                     'author': quote.xpath('span/small/text()').get(),
#                     'text': quote.css('span.text::text').get(),
#                 }

#                 next_page = response.css('li.next a::attr("href")').get()
#                 if next_page is not None:
#                     yield response.follow(next_page, self.parse)

#     def parse(self, response):
#         page = response.css('div').extract()

#         filename = 'quotes-1.txt'
        
#         with open(filename, 'a+') as f:
#             for i in page:
#                 f.write(i + '\n')'''
    