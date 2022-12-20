#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


# 创建一个工资系统
class Person:
    def __init__(self, name, age, pay=0, job=None):  # 初始化类实例的方法
        self.name = name  # self为实例
        self.age = age
        self.pay = pay
        self.job = job


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')  # 产生实例
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name)
    print(sue.pay)

    print(bob.name.split()[-1])  # 查询Lastname
    sue.pay *= 1.10  # 加薪
    print(sue.pay)

