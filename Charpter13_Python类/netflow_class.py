#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

flow1 = ['1.1.1.1', 23, '2.2.2.2', 1023, 'tcp']

flow2 = {'sip': '1.1.1.1',
         'dip': '2.2.2.2',
         'sport': 23,
         'dport': 1023,
         'protocl': 'tcp'}


class Flow:
    def __init__(self, sip, dip, sport, dport, protocol):
        self.sip = sip
        self.dip = dip
        self.sport = sport
        self.dport = dport
        self.protocol = protocol

    def __str__(self):
        return f'{self.__class__.__name__}Result Flow <source ip: {self.sip}, destination ip: {self.dip}>'


flow3 = Flow('1.1.1.1', '2.2.2.2', 23, 1023, 'tcp')

print(flow1[1])
print(flow1)

print(flow2.get('sip'))
print(flow2)

print(flow3.sip)
print(flow3)

