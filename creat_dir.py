# -*- coding: utf-8 -*-

# Script Name   : creat_dir.py
# Author        : chao yuan
# Created       : 13th January 2017
# Last Modified : 13th January 2017

# Description   : Creat a dirctory in users home directory if there does not exist (在用户的home目录下新建一个文件夹如果该文件夹不存在的话)

import os
import sys


def usage():
    print('[-] Usage: python creat_dir.py <dirname> ')
    exit(0)

def creat_dir(dir_name):
    '''
    Creat a dir by the given dir_name in the user's home directory
    '''
    home = os.path.expanduser('~')
    print(home)
    path = os.path.join(home, dir_name)
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("The directpry does exist!")


def main():
    '''
    Call the main method
    '''
    if len(sys.argv) >= 2:
         dir_name = sys.argv[1]
         creat_dir(dir_name)
    else:
        usage()
   

if __name__ == '__main__':
    main()
