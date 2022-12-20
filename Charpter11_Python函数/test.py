#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# def qytang(x):
#     print(x * 2)
#
# def qytang_r(x):
#     return x * 2
#
# # qytang(2)
#
# # result = qytang_r(2)
# # print(result)
#
# qytang_l = [lambda x:x*2, lambda x:x*4]
#
# result = qytang_l[1](2)
# print(result)


# def times(x,y):
#     return x*y
#
# print(times([1],'qytang'))

def intersect(part1, part2):
    res = []
    for a in part1:
        if a in part2:
            res.append(a)

    return res
#
s1 = 'qytang'
s2 = ['p', 'y']

print(intersect(s1, s2))

# def f(a):
#     # a = 88
#     a = 99
#
# b = 88
#
# f(b)
# print(b)

# def changer(a,b):
#     a = 1
#     a = 2
#     b[0] = 'qytang'
#
# X = 1
# L = [1,2]
#
# changer(X,L)
#
# print(X)
# print(L)

# def f(a, b, c):
#     print(a, b, c)
#
# # f(1,2,3)
# f(1, c=6,b=4)


# def f(a, b=2, port=22):
#     print(a, b, port)
#
# f(1, 3, 2222)

# def f(**qyt_args):
#     print(qyt_args)
#
# f(a=1, b=2, c=3)

# def f(a, b, c):
#     print(a, b ,c)
#
# d = {'a':1, 'b':2, 'c':3}
# f(**d)

# def f(*qyt_list, **qyt_dict):
#     print(qyt_list, qyt_dict)
#
# f(1,2,3,4,5,6,67, x=1, y=2, z=3)
#
# import datetime

import sys
print(sys.path)