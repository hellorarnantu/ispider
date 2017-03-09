# -*- coding: utf-8 -*-

# Scrapy settings for ispider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#


# 取消s3方式
DOWNLOAD_HANDLERS = {
    's3': None,
}

BOT_NAME = 'ispider'

SPIDER_MODULES = ['ispider.spiders']
NEWSPIDER_MODULE = 'ispider.spiders'

#中间组件
ITEM_PIPELINES = {
    'ispider.pipelines.ISpiderPipeline': 303,  # 存储通道
    # 'scrapy.pipelines.images.ImagesPipeline': 301  # 激活图片组件
}

# 爬取间隔时间(防止爬出网站的服务器压力过大)
DOWNLOAD_DELAY = 0.25

COOKIES_ENABLED = True

# 超时时间
DOWNLOAD_TIMEOUT = 5

# 日志级别(包含及其以上)
LOG_LEVEL = 'INFO'

# 日志存放位置
# LOG_STDOUT = True 表示标准输出打印到日志中
# LOG_FILE = '/var/log/ispider/spiders.log'

# 图片存放位置(需要激活图片组件)
# IMAGES_STORE = '/home/zmy/wangpanjun/ispider'
# IMAGES_THUMBS = {
#     'small': (300, 300),
#     'big': (500, 500),
# }

# 最大并发量(缓解服务器压力)
CONCURRENT_REQUESTS_PER_DOMAIN = 10

# 开启代理
DOWNLOADER_MIDDLEWARES = {
    # 'ispider.misc.middleware.CustomHttpProxyMiddleware': 400,
    'ispider.misc.middleware.CustomUserAgentMiddleware': 401,
}
# 爬取的最大深度
DEPTH_LIMIT = 2
# DNSCACHE_ENABLED = False
# COMMANDS_MODULE = 'ispider.commands'



# MYSQL_HOST = '47.93.39.190'
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'ineww'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'