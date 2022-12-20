#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


class Netflow:
    def __init__(self, flowid, sip, dip, sport, dport, pro):
        self.flowid = flowid
        self.sip = sip
        self.dip = dip
        self.sport = sport
        self.dport = dport
        self.pro = pro

    def __str__(self):
        return f'<{self.__class__.__name__} = flowid:{self.flowid}, sip:{self.sip}, dip:{self.dip}>'


if __name__ == '__main__':
    flow1 = Netflow(123123123, '1.1.1.1', '2.2.2.2', '1023', '23', 'TCP')
    print(flow1.sip)
    print(flow1)
    flow2 = {123123123: {'sip': '1.1.1.1', 'dip': '2.2.2.2'}}
    print(flow2.get(123123123).get('sip'))
    print(flow2)
