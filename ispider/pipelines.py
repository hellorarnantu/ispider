# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi

import logging
import MySQLdb
import MySQLdb.cursors


class ISpiderPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        print dbargs

        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def open_spider(self, spider):
        logging.info(u"～～～Spider 开始～～～")

    def process_item(self, item, spider):
        for key, value in item.items():
            item[key] = value[0]
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)

    def _do_upinsert(self, conn, item, spider):

        insert_sql = "insert into news(" \
             "title, content, reading_number, agree_number, disagree_number, " \
             "category, keywords, author, original, created_time,source, image)" \
             " values ('%s', '%s', 0, 0, 0, 0, '%s', '%s', '%s', '%s', '%s', '%s')" % (item['title'],
                                                                                       str(item['content']),

                                                                                       item['keywords'],
                                                                                       item['author'],
                                                                                       item["original"],
                                                                                       item['created_time'],
                                                                                       item["source"],
                                                                                       item['image'])
        conn.execute(insert_sql)

    def close_spider(self, spider):
        logging.info(u"～～～Spider 结束～～～")

    def _handle_error(self, failue, item, spider):
        print failue
        # log.err(failure)
