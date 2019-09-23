# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/22 19:12
Desc:
'''

import pymongo
from pymongo.errors import DuplicateKeyError


class MongoDB():

    def __init__(self):
        # 连接mongodb服务器,先启动mongodb服务器和客户端
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        # 连接ProxiesPool数据库，可以先在mongodb中创建ProxiesPool数据库，集合插入数据时会自动创建
        self.db = self.client['ProxiesPool']
        # 连接ProxiesPool数据库下的proxies集合
        self.proxies = self.db['proxies']
        # 给proxy字段创建一个新的索引，加快查询的速度
        self.proxies.ensure_index('proxy', unique=True)

    # 插入数据
    def insert(self, proxy):
        try:
            self.proxies.insert(proxy)
            print("插入成功:{}".format(proxy))
        except DuplicateKeyError:
            pass

    # 删除数据
    def delete(self, conditions):
        self.proxies.remove(conditions)
        print("删除成功:{}".format(conditions))

    # 更新数据
    def update(self, conditions, values):
        self.proxies.update(conditions, {"$set": values})
        print("更新成功:{},{}".format(conditions, values))

    # 取出所有的数据，count是check_crawl_ip获取到的ip代理数量
    def get(self, count, conditions=None):
        conditions = conditions if conditions else {}
        count = int(count)
        items = self.proxies.find(conditions)  # conditions=None,即默认查找所有的proxies集合下所有的文档
        # 取出数据，按delay进行排序，延时小的放在列表前面，用的时候可以先拿出来
        # items = self.proxies.find(conditions, limit=count).sort("delay", pymongo.ASCENDING)
        items = list(items)
        return items

    # 统计数据库中代理个数
    def get_count(self):
        return self.proxies.count({})  # {}条件为空，即统计全部数据


if __name__ == '__main__':
    mongodb = MongoDB()
    print(mongodb.get(3))

# db.proxies.find().sort("delay", pymongo.ASCENDING)