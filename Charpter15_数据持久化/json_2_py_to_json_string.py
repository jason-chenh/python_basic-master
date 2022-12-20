#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import json
from source_db import qyt_teachers  # 导入字典
from datetime import datetime
from pprint import pprint
print(qyt_teachers)  # 打印字典
# pprint是对Python对象美化后的打印
pprint(qyt_teachers, indent=4)
print(type(qyt_teachers))

# qyt_teachers.update({'dateteime': datetime.now()})
qyt_teachers.update({'bool': True})

# json.dumps, indent=4, 也是一种美化的处理
json_string = json.dumps(qyt_teachers, ensure_ascii=False, indent=4)
# json_string = json.dumps(qyt_teachers, ensure_ascii=False)
print(json_string)
print(type(json_string))

dict_recv = json.loads(json_string)
print(dict_recv)
print(type(dict_recv))



