# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/23 20:44
Desc: 主进程调度器
'''

from multiprocessing import Process
from Crawler.check_crawl_ip import CheckIp, CrawlIp
from api import run


def proxy_run():

    # 数据库中ip检测进程
    check_process = Process(target=CheckIp().check)
    # 爬取ip代理的进程
    crawl_process = Process(target=CrawlIp().crawl)
    # api接口进程，用于从数据库中取出一个或者全部ip代理
    run_process = Process(target=run)

    # 启动所有进程
    check_process.start()
    crawl_process.start()
    run_process.start()

    # 等待所有进程结束
    check_process.join()
    crawl_process.join()
    run_process.join()


if __name__ == '__main__':
    proxy_run()
