# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class JianshuArticlePipeline(object):
    def open_spider(self, spider):
        self.file = open('jianshu.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        if(type(item)!=dict):
            item = dict(item)
        str_data = json.dumps(item,ensure_ascii=False) + ',\n'
        self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()