#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import sqlite3

conn = sqlite3.connect('./sqlite_dir/qytanghomework.sqlite')
cursor = conn.cursor()

user_notify = """
请输入查询选项:
输入 1 : 查询整个数据库
输入 2 : 基于姓名查询
输入 3 : 基于年龄查询
输入 4 : 基于作业数查询
输入 0 : 退出
"""
while True:
    print(user_notify)
    user_input = input('请选择:')
    if user_input == '0':
        break
    elif user_input == '1':
        cursor.execute("select * from qytang_homework_info")
        yourresults = cursor.fetchall()

        for teacher in yourresults:
            print('学员姓名:{0:<6}  学员年龄:{1:<3}  学员作业数:{2:<3}'.format(teacher[0], teacher[1], teacher[2]))

    elif user_input == '2':
        user_sn = input('请输入学员姓名:')
        if not user_sn:
            continue
        cursor.execute("select * from qytang_homework_info where 姓名='{0}'".format(user_sn))
        yourresults = cursor.fetchall()
        if not yourresults:
            print('学员信息未找到!')
        for teacher in yourresults:
            print('学员姓名:{0:<6}  学员年龄:{1:<3}  学员作业数:{2:<3}'.format(teacher[0], teacher[1], teacher[2]))
    elif user_input == '3':
        user_age = input('搜索大于输入年龄的学员,请输入学员年龄:')
        if not user_age:
            continue
        cursor.execute("select * from qytang_homework_info where 年龄>{0}".format(user_age))
        yourresults = cursor.fetchall()
        if not yourresults:
            print('学员信息未找到!')
        for teacher in yourresults:
            print('学员姓名:{0:<6}  学员年龄:{1:<3}  学员作业数:{2:<3}'.format(teacher[0], teacher[1], teacher[2]))
    elif user_input == '4':
        user_homework = input('搜索大于输入作业数的学员,请输入作业数量:')
        if not user_homework:
            continue
        cursor.execute("select * from qytang_homework_info where 作业数>{0}".format(user_homework))
        yourresults = cursor.fetchall()
        if not yourresults:
            print('学员信息未找到!')
        for teacher in yourresults:
            print('学员姓名:{0:<6}  学员年龄:{1:<3}  学员作业数:{2:<3}'.format(teacher[0], teacher[1], teacher[2]))
    else:
        print('输入错误!请重试!')

