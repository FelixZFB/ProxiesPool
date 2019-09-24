# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/23 21:14
Desc:
'''

import requests
import json

# 调用ip代理接口地址
PROXY_POOL_URL = 'http://127.0.0.1:5000/one'  # one proxy
PROXIES_POOL_URL = 'http://127.0.0.1:5000/all'  # all proxies

# 数据库中取出一个ip
def get_one_proxy():
    try:
        ip_proxy = PROXY_POOL_URL
        response = requests.get(ip_proxy)
        if response.status_code == 200:
            return json.loads(response.text)
    except ConnectionError:
        return None

def get_all_proxy():
    try:
        ip_proxy = PROXIES_POOL_URL
        response = requests.get(ip_proxy)
        if response.status_code == 200:
            return json.loads(response.text)
    except ConnectionError:
        return None

print(get_one_proxy())
print(type(get_one_proxy()))
print()
print(get_all_proxy())
print(type(get_all_proxy()))

# 输出结果是字典和列表：
# {"proxy": "117.196.232.216:8080"}
# ["118.163.96.167:3129", "116.196.90.181:3128", "42.115.221.58:3128", "47.99.65.77:8118", "117.196.232.216:8080", "101.109.255.48:32414", "115.127.62.36:8080"]
