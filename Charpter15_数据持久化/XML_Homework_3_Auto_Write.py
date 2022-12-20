#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from xml.dom.minidom import Document
from XML_Homework_0_Dict import qytang_dict

# 创建根
doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

# 创建公司
qytang_commany = doc.createElement('公司')
qytang_commany.setAttribute('name', '亁颐堂')
root.appendChild(qytang_commany)

# 循环写入部门(可能有多个部分)
for sub_depart in qytang_dict.get('公司').get('亁颐堂').get('部门'):
    # 创建部门, 并且写入部门名
    department = doc.createElement('部门')
    department.setAttribute('name', sub_depart.get('部门名'))
    qytang_commany.appendChild(department)

    # 创建师资
    teachers = doc.createElement('师资')
    department.appendChild(teachers)

    # 循环写入老师名
    for teacher in sub_depart.get('师资'):
        teacher_name = doc.createElement('老师')
        teacher_name.setAttribute('name', teacher)
        teachers.appendChild(teacher_name)

    # 创建课程
    courses = doc.createElement('课程')
    department.appendChild(courses)

    # 循环写入课程名
    for course in sub_depart.get('课程'):
        course_name = doc.createElement('课程名')
        course_name.setAttribute('name', course)
        courses.appendChild(course_name)

# 写入到文件
xml_file = open('XML_Homework_AutoCreate.xml', 'w',  encoding='utf-8')
xml_file.write(doc.toprettyxml(indent='    '))
xml_file.close()
