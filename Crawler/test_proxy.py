# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/22 19:38
Desc: 测试ip代理是否有效
'''

import requests
import time
from requests.exceptions import ProxyError, ConnectionError
from MongoDB.mongo_db import MongoDB
from multiprocessing.pool import ThreadPool


class TestIp():

    def test_all(self, proxy_list, method):
        # 进程池中同时最多16个进程，数据库中取出的是所有IP的一个列表
        pool = ThreadPool(16)
        # 向进程池中添加任务
        for proxy in proxy_list:
            pool.apply_async(self.test_one, args=(proxy, method))
        # 关闭进程池，不在接受新的任务
        pool.close()
        # 等待所有子进程结束
        pool.join()

    def test_one(self, proxy, method):
        url = 'https://www.baidu.com'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        proxies = {
            'http': 'http://' + proxy['proxy'],
            'https': 'http://' + proxy['proxy']
        }
        try:
            start_time = time.time()
            resp = requests.get(url, headers=headers, proxies=proxies, timeout=5, verify=True)
            # 记录ip代理请求用时
            delay = round(time.time() - start_time, 2)
            #
            if resp.status_code == 200:
                # 把delay加入到proxy字典中
                proxy['delay'] = delay
                if method == 'insert':
                    # 插入代理到数据库
                    MongoDB().insert(proxy)
                elif method == 'check':
                    MongoDB().update({'proxy': proxy['proxy']}, {'delay': proxy['delay']})
            else:
                print("无效ip:{}".format(proxy))
                if method == 'check':
                    MongoDB().delete({'proxy': proxy['proxy']})
        except (ProxyError, ConnectionError):
            print("无效ip:{}".format(proxy))
            if method == 'check':
                MongoDB().delete({'proxy': proxy['proxy']})
        except Exception:
            # traceback.print_exc()
            pass
