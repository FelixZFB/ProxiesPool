'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/23 20:44
Desc: ProxiesPool IP代理池
'''

# ProxiesPool IP代理池
# MongoDB和flask实现的一个IP代理池

# 实现逻辑：
    - 1.爬取免费代理IP网站（西刺代理，快代理，66代理等）的高匿代理
    - 2.检测出有效的高匿代理，存储到MongoDB数据库中
    - 3.定时检测MongoDB数据库已有IP代理是否有效，进行更新删除
    - 4.使用flask的api接口调用IP代理池中的IP代理

# 启动方式:
    - 1.启动本地MongoDB数据库
    - 2.运行main.py
    - 3.外部api调用
    -

# 外部调用方式：
参考api_demo.py
```python
import requests

PROXY_POOL_URL = 'http://127.0.0.1:5000/one'  # one proxy
PROXIES_POOL_URL = 'http://127.0.0.1:5000/all'  # all proxies

```

# http://localhost:5000/one  one一个代理对应是字典,取出字典的值就可以使用
# {"proxy": "117.67.3.60:61234"}

# http://127.0.0.1:5000/all all全部代理对应的是一个列表，直接随机取出列表中的一个值使用
# ["104.207.152.40:3128", "171.37.78.41:9797", "119.120.180.34:61234", "120.84.100.253:9999"]