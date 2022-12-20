#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import paramiko
import socket


def qytang_ssh(ip, username, password, port=22, cmd='show run'):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        if 'Line has invalid autocommand' in x:
            print('命令不能被执行！请检查用户权限！')
        else:
            return x

    except paramiko.ssh_exception.AuthenticationException as e:
        print('认证错误', e)
    except socket.timeout as e:
        print('连接超时', e)
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print('SSH请求被管理过滤', e)


if __name__ == '__main__':
    print(qytang_ssh('10.1.1.11', 'admin', 'Cisc0123'))
