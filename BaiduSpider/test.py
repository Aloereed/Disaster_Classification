'''
Author: HU Zheng
Date: 2021-04-16 12:10:39
LastEditors: HU Zheng
LastEditTime: 2021-04-20 13:56:38
Description: file content
'''
from baiduspider import BaiduSpider
from pprint import pprint
spider = BaiduSpider()
dict = spider.search_news(query='灾害',pn=20)
pprint(dict)

