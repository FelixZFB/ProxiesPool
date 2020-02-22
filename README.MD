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
        - 程序启动后会自动爬取，自动更新数据库中IP代理，保持代理不断更新可用
        - 代理很快失效，程序一直启动着，可用代理就会不断增加

# 启动方式:
    - 1.启动本地MongoDB数据库(管理员运行CMD，net start mongodb启动服务，然后mongo连接服务)
    - 2.然后运行main.py主程序，启动代理
    - 3.外部api调用

# 外部调用IP代理池方式：
参考api_demo.py
```python
import requests

PROXY_POOL_URL = 'http://127.0.0.1:5000/one'  # one proxy，一个字典，PROXY_POOL_URL={"proxy": "117.67.3.60:61234"}
PROXIES_POOL_URL = 'http://127.0.0.1:5000/all'  # all proxies，列表，PROXIES_POOL_URL=["104.207.152.40:3128", "171.37.78.41:9797", "119.120.180.34:61234", "120.84.100.253:9999"]

```

# http://localhost:5000/one  one一个代理对应是字典,取出字典的值就可以使用
# {"proxy": "117.67.3.60:61234"}

# http://127.0.0.1:5000/all all全部代理对应的是一个列表，直接随机取出列表中的一个值使用
# ["104.207.152.40:3128", "171.37.78.41:9797", "119.120.180.34:61234", "120.84.100.253:9999"]