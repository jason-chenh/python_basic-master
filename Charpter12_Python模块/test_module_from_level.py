#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import level1

level1.l1_printer(2, 3)

from level1.level1_module import l1_module_printer
l1_module_printer('test!')

from level1.level2 import l2_a, l2_printer
from level1.level2.level2_module import l2_module_printer, l2_c

l2_printer(l2_c)
l2_module_printer(l2_a)





