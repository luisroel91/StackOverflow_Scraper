# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

from soscraper.items import SoscraperItem


class SoSpider(scrapy.Spider):
    name = 'sospider'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        'http://stackoverflow.com/questions?pagesize=50&sort=newest',
    ]

    def parse(self, response):
        questions = scrapy.Selector(response).xpath('//div[@class="summary"]')
        views = scrapy.Selector(response).xpath('//div[@class="views "]')

        for question, view in zip(questions, views):
            item = SoscraperItem()
            item['question_title'] = question.xpath('h3/a[@class="question-hyperlink"]/text()').extract()
            item['question_url'] = question.xpath('h3/a[@class="question-hyperlink"]/@href').extract()
            item['question_excerpt'] = question.xpath('div[@class="excerpt"]/text()').extract()
            item['view_count'] = view.xpath('@title').extract()

            yield item
