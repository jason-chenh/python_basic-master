#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import subprocess
import io


def system_cmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    proc.wait()
    stream_stdout = io.TextIOWrapper(proc.stdout)
    stream_stderr = io.TextIOWrapper(proc.stderr)

    str_stdout = str(stream_stdout.read())
    str_stderr = str(stream_stderr.read())

    return str_stdout, str_stderr


if __name__ == "__main__":
    exec_cmd = 'pwd'
    print(system_cmd(exec_cmd))
    exec_cmd = 'pwd1'
    print(system_cmd(exec_cmd))
    import datetime
    datetime.datetime.now() - datetime.timedelta(minutes=3)