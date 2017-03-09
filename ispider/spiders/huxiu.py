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
    name = 'huxiuspider'

    start_urls = [
        # 'http://www.huxiu.com'
        "https://www.huxiu.com/article/184246.html?f=retweeted"
    ]

    # rules = [
    #     Rule(LinkExtractor(allow='/article/(\d)*.html'),
    #          callback='parse_item', follow=False),
    # ]

    def parse(self, response):
        logging.info(u"start crawl  --->  " + response.url)
        item = ItemLoader(item=NewsItem(), response=response)
        images = []
        sel = Selector(response)
        item.add_xpath('keywords', "//head/meta[@name='keywords']/@content")
        if sel.xpath('//div[@class="neirong-shouquan"]'):
            return
        item.add_xpath('title', '//div[@class="article-wrap"]/h1/text()')
        item.add_xpath('author', '//span[@class="author-name"]/text()')
        item.add_value('source', u'虎嗅网')
        item.add_value('original_link', response.url)
        item.add_value('category', CATEGORY.TECHNOLOGY)
        article_time = sel.xpath('//span[@class="article-time"]/text()').extract()
        date_time = compare_time(article_time, "%Y-%m-%d %H:%M")
        # if not date_time:
        #     return
        item.add_value('date_time', article_time)
        image_url = sel.xpath('//div[@class="article-img-box"]/img/@src').extract()[0]
        images.append(image_url)
        elements = sel.xpath('//div[@id="article_content"]/p').extract()
        images, content = translate_content(elements)
        if images:
            item.add_value('image_url', hashlib.sha1(images[0]).hexdigest() + ".jpg")
        item.add_value('image_urls', images)
        item.add_value('content', content)
        print content
        logging.info(u"finished crawl  --->  " + response.url)
        yield item.load_item()
