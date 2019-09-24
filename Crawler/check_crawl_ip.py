# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/23 15:58
Desc:
'''

import time
from Crawler.get_proxy import GetProxy
from Crawler.test_proxy import TestIp
from MongoDB.mongo_db import MongoDB
from multiprocessing import Process


class CheckIp():

    def __init__(self):
        pass

    def check(self):
        # 启动循环不断检测数据库中代理的可用性
        while True:
            # 创建一个实例，获取数据库中代理个数
            mongo = MongoDB()
            count = mongo.get_count()
            # 如果有数据，进行代理检测
            if not count == 0:
                print('开始检测数据库中的代理是否可用>>>>>>>>>>>>>>>>')
                # 取出所有的代理
                proxies = mongo.get(count)
                # 测试所有ip是否有效，传入的是proxies列表和check方法
                # 根据检测结果无效就删除，有效的话就进行更新，更新delay键对应的值
                TestIp().test_all(proxies, 'check')
            # 添加定时功能，每10分钟检测一次所有代理ip是否有效，时间可以调整
            else:
                pass
            time.sleep(60 * 10)


class CrawlIp():

    def __init__(self):
        pass

    def crawl(self):
        # 启动循环不断爬取ip代理，代理网站ip代理是不断的在更新中
        while True:
            print('开始从代理IP网站爬取可用的代理IP到本地数据库>>>>>>>>>>>>>>>>>>')
            # 先爬取各大代理网站，get_proxy的每个方法可以返回代理ip的列表
            # 但是时间长了，list会超过rangge，内存会被消耗殆尽
            # 因此改造为yield生成器，每生成一个，检测一个
            # 每个代理网站单独开一个进程，同时多个网站同时爬取

            # xici_list = GetProxy().xici_proxy()
            # kuai_list = GetProxy().kuai_proxy()
            # liuliu_list = GetProxy().liuliu_proxy()

            # 检查爬取的列表是否有效，有效就使用insert方法插入到数据库中
            # TestIp().test_all(xici_list, "insert")
            # TestIp().test_all(kuai_list, "insert")
            # TestIp().test_all(liuliu_list, "insert")

            xici_process = Process(target=self.xici_process)
            kuai_process = Process(target=self.kuai_process)
            liuliu_process = Process(target=self.liuliu_process)

            xici_process.start()
            kuai_process.start()
            liuliu_process.start()

            xici_process.join()
            kuai_process.join()
            liuliu_process.join()

            print("所有代理网站一次爬取完成，等待下一次爬取自动启动>>>>>>>>>>>>>>>>>>")
            # 添加定时功能，每60分钟所有网站在爬取一遍，时间可以调整
            time.sleep(60 * 10)


    def xici_process(self):
        for proxy in GetProxy().xici_proxy():
            # GetProxy().xici_proxy()返回值是一个yield字典，for循环不断调出取用
            # 检测接收的是一个列表参数，直接使用一个空列表即可
            print("西刺代理：%s" % proxy)
            proxy_list = []
            proxy_list.append(proxy)
            TestIp().test_all(proxy_list, "insert")

    def kuai_process(self):
        for proxy in GetProxy().kuai_proxy():
            print("快代理：%s" % proxy)
            proxy_list = []
            proxy_list.append(proxy)
            TestIp().test_all(proxy_list, "insert")

    def liuliu_process(self):
        for proxy in GetProxy().liuliu_proxy():
            print("六六代理：%s" % proxy)
            proxy_list = []
            proxy_list.append(proxy)
            TestIp().test_all(proxy_list, "insert")


if __name__ == '__main__':
    crawl = CrawlIp()
    crawl.crawl()

    # check = CheckIp()
    # check.check()
