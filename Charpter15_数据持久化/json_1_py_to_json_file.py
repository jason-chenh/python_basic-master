#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import json
from source_db import qyt_teachers, qyt_courses  # 导入字典


print('把Python对象转换为JSON格式，并且写入文件')
with open('./json_dir/json_0_qyt_teachers.json', 'w', encoding='utf-8') as f:
    json.dump(qyt_teachers, f, ensure_ascii=False)  # 不要确认所有的字符都能够被ASCII表示, 因为有中文

with open('./json_dir/json_0_qyt_courses.json', 'w', encoding='utf-8') as f:
    json.dump(qyt_courses, f, ensure_ascii=False)

with open('./json_dir/json_0_true.json', 'w', encoding='utf-8') as f:
    json.dump({"qytang": True}, f, ensure_ascii=False)


qyt_f = open('./json_dir/json_0_qyt_teachers.json', 'r', encoding='utf-8')
new_dict = json.load(qyt_f)
print(new_dict)
