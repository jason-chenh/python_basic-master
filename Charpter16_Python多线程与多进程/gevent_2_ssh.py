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

from ssh_client import ssh_client_no_async

import gevent
from gevent import monkey

monkey.patch_all()


def get_ssh_result(i):
    print("start", i)
    result = ssh_client_no_async('localhost', 'root', 'Cisc0123', 'ls / -an', asy_id=i)
    print("end", i)
    return result


tasks = [gevent.spawn(get_ssh_result, i) for i in range(3)]
all_result = gevent.joinall(tasks)
for x in all_result:
    print(x.get())

    # print(x.get().text)

