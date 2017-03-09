# -*- coding: utf-8 -*-



import hashlib

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule

from ispider.items import NewsItem
import logging
from ispider.config.config import CATEGORY
from ispider.utils.helper import compare_time, translate_content


class NewsSpider(CrawlSpider):
    name = 'sohuspider'

    start_urls = [
        'http://it.sohu.com/internet_2014.shtml'
    ]

    rules = [
        Rule(LinkExtractor(allow='^http://it.sohu.com/(\d*)/(\w*).shtml$'),
             callback='parse_item', follow=False),
    ]

    def parse_item(self, response):
        logging.info(u"start crawl  --->  " + response.url)
        item = ItemLoader(item=NewsItem(), response=response)
        sel = Selector(response)
        item.add_xpath('keywords', "//head/meta[@name='keywords']/@content")
        item.add_xpath('title', '//div[@class="news-title"]/h1/text()')
        item.add_xpath('author', '//span[@class="writer"]/a/text()')
        item.add_value('source', u'搜狐网')
        item.add_value('original', response.url)
        item.add_value('category', CATEGORY.TECHNOLOGY)
        article_time = sel.xpath('//span[@id="pubtime_baidu"]/text()').extract()
        date_time = compare_time(article_time)
        if not date_time:
            return
        item.add_value('created_time', article_time)
        elements = sel.xpath('//div[@id="contentText"]/p').extract()
        images, content = translate_content(elements)
        if images:
            # item.add_value('image', hashlib.sha1(images[0]).hexdigest() + ".jpg")
            item.add_value('image', images[0])
        else:
            item.add_value("image", "")
        # item.add_value('image_urls', images)
        item.add_value('content', content)
        logging.info(u"finished crawl  --->  " + response.url)
        yield item.load_item()
