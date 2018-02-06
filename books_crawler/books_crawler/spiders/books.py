# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    '''
    LinkExtractor arguments ==> deny_domains - avoid the domains to scrape present in the website
                            ==> allow - will scrape the page contain the word in the url
    '''


    rules = (Rule(LinkExtractor(deny_domains=('google.com','facebook.com','twitter.com'),allow=('science')), callback='parse_page', follow=False),)


    def parse_page(self, response):
        pass
