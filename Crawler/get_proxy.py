# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/22 15:54
Desc: get proxy
'''

import time
import requests
import chardet
import traceback
import user_agent
from lxml import etree
from requests.exceptions import ConnectionError


class GetProxy():
    def __init__(self):
        self.headers = {"User-Agent": user_agent.generate_user_agent()}

    # 判断提供ip代理网站是否有效，返回网页html文档
    def parse_url(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.encoding = chardet.detect(response.content)["encoding"]
            if response.status_code == 200:
                return response.text
            else:
                return None
        except ConnectionError:
            print("Error.")
        return None

    # 获取西刺代理网站免费代理ip
    def xici_proxy(self):
        # 加入延时，防止ip被封
        time.sleep(3)
        # 只获取网站高匿代理前20页的代理
        # xici_list = list()
        for i in range(1, 20):
            url = "https://www.xicidaili.com/nn/{}".format(i)
            response = self.parse_url(url)
            # 上面的response类型有时候是NoneType,有些是str，下面使用str(response)
            html = etree.HTML(str(response), etree.HTMLParser())
            # 所有的ip和port都是放在属性为ip_list标签下的tr标签里面
            # ip_list属性唯一，下面两种方式都是选取所有属性id='ip_list'的标签
            ip_list = html.xpath("//table[@id='ip_list']/tr/td[2]/text()")
            port_list = html.xpath("//*[@id='ip_list']/tr/td[3]/text()")

            # ip和port生成一个一一对应的元组列表，然后取出
            for ip, port in zip(ip_list, port_list):
                proxy = ip + ":" + port
                proxy = {"proxy": proxy}  # 返回的代理是字典的格式，方便直接存储到mongodb数据库中
                yield proxy
                # xici_list.append(proxy)
        # return xici_list

    # 获取快代理网站免费代理ip
    def kuai_proxy(self):
        # 加入延时
        time.sleep(3)
        # 只获取网站高匿代理前20页的代理
        # kuai_list = list()
        for i in range(1, 20):
            url = "https://www.kuaidaili.com/free/inha/{}/".format(i)
            response = self.parse_url(url)
            # 上面的response类型有时候是NoneType,有些是str，下面使用str(response)
            html = etree.HTML(str(response), etree.HTMLParser())
            # 所有的ip和port都是放在属性为list的div/table/tbody下的tr标签里面
            ip_list = html.xpath("//div[@id='list']/table/tbody/tr/td[1]/text()")
            port_list = html.xpath("//div[@id='list']/table/tbody/tr/td[2]/text()")

            # ip和port生成一个一一对应的元组列表，然后取出
            for ip, port in zip(ip_list, port_list):
                proxy = ip + ":" + port
                proxy = {"proxy": proxy}  # 返回的代理是字典的格式，方便直接存储到mongodb数据库中
                yield proxy
                # kuai_list.append(proxy)
        # return kuai_list

    # 获取快代理网站免费代理ip
    def liuliu_proxy(self):
        # 只获取网站高匿代理前20页的代理
        # liuliu_list = list()
        for i in range(1, 20):
            # 加入延时
            time.sleep(3)
            url = "http://www.66ip.cn/{}.html".format(i)
            response = self.parse_url(url)
            # 上面的response类型有时候是NoneType,有些是str，下面使用str(response)
            html = etree.HTML(str(response), etree.HTMLParser())
            # 所有的ip和port都是放在属性为list的div/table/tbody下的tr标签里面,列表第一个元素是标题栏，去除掉
            ip_list = html.xpath("//div[@class='containerbox boxindex']/div[1]/table[1]//tr/td[1]/text()")[1:]
            port_list = html.xpath("//div[@class='containerbox boxindex']/div[1]/table[1]//tr/td[2]/text()")[1:]

            # ip和port生成一个一一对应的元组列表，然后取出
            for ip, port in zip(ip_list, port_list):
                proxy = ip + ":" + port
                proxy = {"proxy": proxy}  # 返回的代理是字典的格式，方便直接存储到mongodb数据库中
                yield proxy
                # liuliu_list.append(proxy)
        # return liuliu_list

    # 自己可以扩充代理网站
    def other_proxy(self):
        pass


if __name__ == '__main__':
    res = GetProxy().liuliu_proxy()
    print(res)
    for i in res:
        print(type(i))
        print(i)

    # print(res.__next__())
    # print(res.__next__())
    # print(res.__next__())
