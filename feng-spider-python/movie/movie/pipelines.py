# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MoviePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='fengj', passwd='gogg897@!', db='Content',
                                    charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute("truncate table Movie")
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into Movie (name,movieInfo,star,quote,url,intro) VALUES (%s,%s,%s,%s,%s,%s)", (
                item['title'], item['movieInfo'], item['star'], item['quote'], item['url'], item['intro']))
            self.conn.commit()
        except pymysql.Error:
            print("Error%s,%s,%s,%s" % (item['title'], item['movieInfo'], item['star'], item['quote']))
        return item
