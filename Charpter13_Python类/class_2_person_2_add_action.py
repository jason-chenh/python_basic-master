#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def getlastname(self):  # 添加查询lastname的行为
        return self.name.split()[-1]

    def giveraise(self, percent):  # 添加加薪的行为
        # self.pay *= (1.0 + percent)
        self.pay = int(self.pay * (1.0 + percent))


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)

    print(bob.getlastname())
    sue.giveraise(0.1)
    print(sue.pay)
