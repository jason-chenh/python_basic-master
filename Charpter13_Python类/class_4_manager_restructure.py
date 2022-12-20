#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from class_2_person_2_add_action import Person


class Manager(Person):
    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)


if __name__ == '__main__':
    # bob = Person('Bob Smith', age=42, pay=3000)
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    tom.giveraise(.20)
    # print(bob.pay)
    print(tom.pay)
    # # print(tom.getlastname())
    # # tom.giveraise(.20)
    # # print(tom.pay)
    #
    # bob.giveraise(0.1)
    # tom.giveraise(0.1)
    # print(bob.pay)
    # print(tom.pay)
