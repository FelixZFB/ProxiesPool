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

# 调用ip代理接口地址
PROXY_POOL_URL = 'http://localhost:5000/one'  # one proxy
PROXIES_POOL_URL = 'http://127.0.0.1:5000/all'  # all proxies

def get_one_proxy():
    try:
        ip_proxy = PROXY_POOL_URL
        response = requests.get(ip_proxy)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None

def get_all_proxy():
    try:
        ip_proxy = PROXIES_POOL_URL
        response = requests.get(ip_proxy)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None

print(get_one_proxy())
print(get_all_proxy())
