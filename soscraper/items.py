# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question_title = scrapy.Field()
    question_url = scrapy.Field()
    question_excerpt = scrapy.Field()
    view_count = scrapy.Field()
