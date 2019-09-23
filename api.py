# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/9/22 19:40
Desc: 外部api接口
'''

import flask
import json
from MongoDB.mongo_db import MongoDB
import random

app = flask.Flask(__name__)


# 从数据库中获取一个ip代理
@app.route('/one')
def get_one():
    proxies = MongoDB().get(1)
    # 所有代理数量减去一个，然后从result列表随机取出1个，MongoDB().get条件为None，取出的是所有的ip代理
    result = [proxy['proxy'] for proxy in proxies]
    x = random.randint(0, MongoDB().get_count() - 1)
    # 返回json格式的类似字典的字符串
    return json.dumps(dict(proxy=result[x]) )

# 从数据库中获取所有的ip代理
@app.route('/all')
def get_all():
    #  http://127.0.0.1:5000/many?count=2
    # args = flask.request.args  # 参数提交
    proxies = MongoDB().get(1)
    result = [proxy['proxy'] for proxy in proxies]
    # x = random.randint(1,MongoDB().get_count()-1)

    # 返回json格式的类似列表的字符串
    return json.dumps(result)


@app.route('/delete')
def delete():
    args = flask.request.args
    MongoDB().delete({'proxy': args['proxy']})
    return '删除成功：{}'.format(args)


def run():
    app.run()
