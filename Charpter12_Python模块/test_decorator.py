#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# https://foofish.net/python-decorator.html

from functools import wraps


def write_to_file(filename):
    def decorator(func):
        @wraps(func)  # 保持func.__name__ func.__doc__
        def with_write_to_file(*args, **kwargs):  # (*args, **kwargs) 可以接受任意参数
            # 装饰器添加的功能
            get_result = func(*args, **kwargs)
            wf = open(filename, 'w')
            wf.write(get_result)
            wf.close()
            # 装饰器添加的功能
            return get_result  # 返回函数运行结果

        return with_write_to_file  # 返回函数 + 写入返回内容到文件

    return decorator  # 返回函数 + 写入返回内容到文件 + 保持func.__name__ func.__doc__


if __name__ == '__main__':
    pass
