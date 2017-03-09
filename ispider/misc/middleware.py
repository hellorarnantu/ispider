# -*- coding: utf-8 -*-



import random
from ispider.misc.agent import AGENTS
from ispider.misc.proxy import PROXIES


class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent

#
# class CustomHttpProxyMiddleware(object):
#
#     def process_request(self, request, spider):
#         p = random.choice(PROXIES)
#
#         request.meta['proxy'] = "http://%s" % p['ip_port']


