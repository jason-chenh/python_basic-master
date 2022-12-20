#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import xmltodict
from pprint import pprint
import json
from xml.dom import minidom


xml_file = open('./xml_dir/xml_1_xml.xml', 'r').read()  # 打开分析的XML文件

xmldict = xmltodict.parse(xml_file, encoding='utf-8')  # 读取xml并转换到OrderedDict字典[有序字典]
pprint(xmldict)
# 不推荐转换到字典
# real_dict = json.loads(json.dumps(xmldict)) # 转换OrderedDict字典到字典, 其实OrderedDict修改方式和字典相同
#
# pprint(real_dict)
#
# sec_teachers = real_dict['root']['公司']['部门'][1]['师资']['老师']  # 提取老师
# for sec_teacher in sec_teachers:
#     print(sec_teacher['@name'])
#
# real_dict['root']['公司']['部门'][1]['@name'] = '乾颐堂安全'  # 修改内容

# 推荐直接对OrderedDict字典进行处理
departments = xmldict['root']['公司']['部门']

for depart in departments:
    print(depart['@name'])

sec_teachers = xmldict['root']['公司']['部门'][1]['师资']['老师']  # 提取老师
for sec_teacher in sec_teachers:
    print(sec_teacher['@name'])
#
xmldict['root']['公司']['部门'][1]['@name'] = '乾颐堂安全'  # 修改内容


# 写回到XML
XML_File = open('./xml_dir/xml_1_xmltodict.xml', 'w', encoding='utf-8')
# XML_File.write(minidom.parseString(xmltodict.unparse(real_dict)).toprettyxml(indent='    '))
XML_File.write(minidom.parseString(xmltodict.unparse(xmldict)).toprettyxml(indent='    '))
XML_File.close()

