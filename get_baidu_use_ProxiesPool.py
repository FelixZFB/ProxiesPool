# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/24 10:53
Desc:
'''

# -*- coding: utf-8 -*-

#导入random，对ip池随机筛选
# 多ip代理模式
import requests
import random
import json
import user_agent
from retrying import retry

class GetUrl():

    def __init__(self):
        self.PROXIES_POOL_URL = 'http://127.0.0.1:5000/all'
        self.headers = {'User-Agent': user_agent.generate_user_agent()}
        self.url = 'https://www.baidu.com/'

    def proxy(self):
        # 为了保持代理池中的ip代理有效，定时要进行检测
        ip_list = json.loads(requests.get(self.PROXIES_POOL_URL).text)
        # print(len(ip_list))
        # 从ip代理池中随机选择一个ip代理
        proxy = {
            'http': 'http://' + random.choice(ip_list),
            'https': 'http://' + random.choice(ip_list),
            }
        # print(proxy)
        return proxy

    # 虽然IP代理池的IP定时进行了检测，但是还是会随时失效
    # 使用重试模块，更换IP进行请求，设置最大重试次数为5次
    @retry(stop_max_attempt_number=5)
    def get_baidu(self):
        print("等待百度响应......")
        # 用IP代理池中的代理请求百度，由于代理速度一般较慢，请求时候加入延时
        response = requests.get(self.url, headers=self.headers, proxies=self.proxy(), timeout=3)
        print("请求成功：%s" % response.status_code)
        # print(response.headers)

if __name__ == '__main__':
    get_url = GetUrl()
    get_url.get_baidu()
