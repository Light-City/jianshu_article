# -*- coding: utf-8 -*-
import scrapy
from jianshu_article.items import JianshuArticleItem


class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']

    user_id = "1b4c832fb2ca"
    url = "https://www.jianshu.com/u/{0}?page=1".format(user_id)
    start_urls = [
        url,
    ]


    def parse(self, response):

        # 不写extract()打印出来就是Selector对象,加上extract()就是返回一个list对象,里面为对应的value,取值可通过.extract()[index]来取得

        # 用户头像
        avatar = response.xpath('//div[@class="avatar"]/img/@src').extract()
        # 昵称
        nickname = response.xpath('//div[@class="author-info"]/div[@class="name"]/text()').extract()
        # 关注及粉丝
        force_fan = response.xpath('//div[@class="author-info"]/div[@class="follow-meta"]/span/text()').extract()
        # 字数及喜欢
        write_love = response.xpath('normalize-space(//div[@class="author-meta"]/text())').extract() # normalize-space去除所有回车换行
        item = JianshuArticleItem()
        item['avatar'] = avatar[0]
        item['nickname'] = nickname[0]
        item['write_love'] = write_love[0]
        item['force'] = force_fan[0]
        item['fan'] = force_fan[1]
        print(item)
        yield item