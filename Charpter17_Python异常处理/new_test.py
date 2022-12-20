#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


def find_index(obj, index):
    try:
        print(obj[index])
    except Exception:
        print('异常')
    else:
        print('不出错打印else')
    finally:
        print('总是打印finally')
#  TypeError: 'int' object is not subscriptable
#  IndexError: string index out of range
#  TypeError: string indices must be integers


if __name__ == '__main__':
    find_index('cisco', 'cisco')
