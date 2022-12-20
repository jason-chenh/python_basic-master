#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import json
from dateutil import parser
from datetime import timedelta

# 源字符串(有问题,需要排错)
test_str_source = "{'姓名': '秦柯', '年龄': 39, '出生日期': '1979-05-05', '状态': true}"
# 修改后字符串
test_str_change = '{"姓名": "秦柯", "年龄": 39, "出生日期": "1979-05-05", "状态": true}'
# 转换字符串到Python字典
test_dict = json.loads(test_str_change)
# 打印字典(第一次打印)
print(test_dict)
# 让我变成80后(出生日期 + 365 * 10 天) ! 提示需要datetime对象的操作
test_dict['出生日期'] = (parser.parse(test_dict['出生日期']).date() + timedelta(days=365 * 10)).strftime("%Y-%m-%d")
# 打印字典(第二次打印)
print(test_dict)
# 写入Python字典到JSON文件
with open('./json_dir/json_homework.json', 'w', encoding='utf-8') as f:
    json.dump(test_dict, f, ensure_ascii=False)
# 读取JSON文件并转换为Python字典
with open('./json_dir/json_homework.json', 'r', encoding='utf-8') as f:
    test_dict_read = json.load(f)
# 打印字典(第三次打印)
print(test_dict_read)
