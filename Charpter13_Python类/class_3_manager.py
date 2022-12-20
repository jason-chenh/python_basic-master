#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from class_2_person_2_add_action import Person


class Manager(Person):  # 继承Person类
    def getfirstname(self):
        return self.name.split()[0]

    def giveraise(self, percent, bonus=0.1):  # 修改giveraise方法
        # self.pay *= (1.0 + percent + bonus)
        self.pay = int(self.pay * (1.0 + percent + bonus))


if __name__ == '__main__':
    # tom = Manager(name='Tom Doe', age=50, pay=50000, job='manager')
    # bob = Person('Bob Smith', 42, 30000, 'software')
    # print(tom.getlastname())
    # print(bob.getlastname())
    # # print(bob.getfirstname())
    # tom.giveraise(0.1)
    # print(tom.pay)
    # bob.giveraise(0.1)
    # print(bob.pay)
    ############################################
    bob = Person(name='Bob Smith', age=42, pay=30000)
    sue = Person(name='Sue Jones', age=45, pay=40000)
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    # print(bob)
    # print(tom)
    print(tom.getfirstname())
    print(tom.getlastname())
    print(bob.getlastname())
    #
    db = [bob, sue, tom]
    for obj in db:
        obj.giveraise(0.1)  # Person和Manager类的实例都拥有giveRaise这个方法
        print(obj.getlastname(), '=>', obj.pay)


