# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    avatar = scrapy.Field()  # 头像
    nickname = scrapy.Field()  # 昵称
    write_love = scrapy.Field() # 字数及喜欢
    fan = scrapy.Field()  # 粉丝
    force = scrapy.Field()  # 关注
