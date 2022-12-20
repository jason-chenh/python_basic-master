#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# https://thief.one/2017/02/20/Python协程/

# gevent vs coroutine
# https://news.ycombinator.com/item?id=22907716

import gevent
from gevent import monkey
monkey.patch_all()
import requests


def get_body(i):
    print("start", i)
    result = requests.get("https://www.baidu.com")
    print("end", i)
    return result


tasks = []

for i in range(3):
    tasks.append(gevent.spawn(get_body, i))

# ip_list = []
# for ip in ip_list:
#     tasks.append(gevent.spawn(qyt_ssh, (ip, 'show run')))
# tasks = [gevent.spawn(get_body, i) for i in range(3)]

all_result = gevent.joinall(tasks)
for x in all_result:
    print(x.get())
    # print(x.get().text)

