#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import paramiko


def ssh_client_no_async(ip, username, password, cmd, asy_id):
    try:
        print('try ssh ' + str(asy_id))
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        ssh.close()
        # await asynico.sleep(1)
        return x

    except Exception as e:
        pass


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    print(ssh_client_no_async('10.1.1.253', 'admin', 'Cisc0123', 'show ver'))

