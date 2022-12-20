#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from xml.etree.ElementTree import parse
from XML_Homework_0_Dict import qytang_dict

tree = parse('XML_Homework_1_XML.xml')  # 打开分析的XML文件

root = tree.getroot()  # 找到根位置
department_list = []
print(dir(root))
for x in root.getchildren():
    print(x.tag)
    print(x.attrib)


for department in root.iter('部门'):
    # 找到部门的名字
    department_dict = {'部门名': department.get('name')}
    teachers_list = []
    # 找到所有老师写入teachers_list
    for teacher in department.iter('老师'):
        teachers_list.append(teacher.get('name'))
    department_dict['师资'] = teachers_list
    courses_list = []
    # 找到所有课程写入courses_list
    for course in department.iter('课程名'):
        courses_list.append(course.get('name'))
    department_dict['课程'] = courses_list
    department_list.append(department_dict)

qytang_dict_parser = {'公司': {'亁颐堂': {'部门': department_list}}}

if __name__ == '__main__':
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(qytang_dict)
    pp.pprint(qytang_dict_parser)