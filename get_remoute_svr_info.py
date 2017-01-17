# -*- coding: utf-8 -*-

# Script Name   : get_remoute_svr_info.py
# Author        : chao yuan
# Created       : 17th January 2017
# Last Modified : 17th January 2017

# Description   : This srcipt will get the infomation of remoute server by ssh(通过ssh连接获取远程服务器的信息)

import subprocess

HOSTS = ['proxy', 'proxy1']  # Get the remoute server's ip address
COMMAND = ['uname -a', 'uptime'] # List the command you want to execute

for host in HOSTS:
    res = []
    for command in COMMAND:
        info = subprocess.Popen(['ssh', '%s'% command], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    res.append(info.stdout.readlines())

    print("---------------" + host + "--------------")
    for r in res:
        if not r:
            print(info.stderr.readlines())
        else:
            print(r)
