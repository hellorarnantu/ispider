# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# from scrapy_djangoitem import DjangoItem
# noinspection PyUnresolvedReferences
# from news.models import News
# from scrapy.item import Field
import scrapy


class NewsItem(scrapy.Item):
    keywords = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    original = scrapy.Field()
    category = scrapy.Field()
    created_time = scrapy.Field()
    image = scrapy.Field()
    # image_urls = scrapy.Field()
    content = scrapy.Field()
    source = scrapy.Field()
