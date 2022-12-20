#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


class Qyt:
    def __init__(self, name_input, age_input):
        self.name = name_input
        self.age = age_input


if __name__ == '__main__':
    qyt1 = Qyt('qinke', 40)
    print(qyt1.name)
    print(qyt1.age)
