#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

qytang_dict = {'公司':
                   {'亁颐堂':
                        {'部门':
                             [{'部门名': 'Python',
                               '师资': ['秦柯', '教主'],
                               '课程': ["Python基础",
                                      "Python网络编程 第一部分 经典协议",
                                      "Python网络编程 第二部分 HTTP协议",
                                      "Python网络编程 第三部分 自动化运维"
                                       ]
                               }
                              ]
                         }
                    }
               }


if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(qytang_dict)