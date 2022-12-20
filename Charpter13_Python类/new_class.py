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

    def getxin(self):
        # print(self.name.split()[0])
        return self.name.split()[0]

    def jiagongzi(self, percent):
        # newpercent = 1 + percent
        # print(newpercent)
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return f'Class类型:{self.__class__.__name__} | 姓名:{self.name} | 年龄:{self.age}'


class Manager(Person):
    def getming(self):
        return self.name.split()[1]

    def jiagongzi(self, percent, bonus=0.1):
        Person.jiagongzi(self, percent + bonus)


if __name__ == '__main__':
    qinke = Manager('QIN KE', 42, 10000)
    ma = Person('Ma HaiBo', 38, 10000)
    print(qinke.name)
    print(ma.pay)

    print(qinke.getxin())
    print(qinke.getming())
    print(ma.getxin())

    for x in [qinke, ma]:
        x.jiagongzi(0.1)

    print(qinke.pay)
    print(ma.pay)

    print(qinke)
    print(ma)
