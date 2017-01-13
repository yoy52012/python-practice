# -*- coding: utf-8 -*-

# Script Name   : automate_backup.py
# Author        : chao yuan
# Created       : 11th January 2017
# Last Modified : 13th January 2017

#Description    ：backup files in the dirctory everyday (备份文件到一个以该日日期命名的文件夹中)

import os
import datetime
import shutil
import argparse

def backup(src_dir, des_dir):
    '''
    recursively backup the file from the src_dir to des_dir with the datetime
    (递归的将所给文件夹内的文件从复制备份到另外一个通过日期命名的文件文件夹中)
    '''

    today = datetime.date.today()   # Get today's date
    todaystr = today.isoformat()    # format the date
    new_dir = os.path.join(des_dir, *("My_Backup", todaystr, ""))   # Get a new dir path using the format date
    if os.path.isdir(src_dir):
        if os.path.exists(src_dir):
            if not os.path.exists(new_dir):
                shutil.copytree(src_dir, new_dir)       # Copy the dirctories
            else:
                print(new_dir + " dose exist!")
        else:
            print(src_dir + " dose not exist!")
    else:
        print("src is not a dir!")


def get_parser():
    '''
    get command line arguments
    (获取命令行参数)
    '''
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='recursively backup the file from the src_dir to des_dir with the datetime')
    parser.add_argument('src_dir', metavar='SRC_DIR', type=str, nargs=1, help='the srcouce dirctory where holds file needed to backup')
    parser.add_argument('des_dir', metavar='DES_EXT', type=str, nargs=1, help='the destination dirctory ')
    return parser


def main():
    '''
    Call the main method
    '''
    parser = get_parser()
    args = vars(parser.parse_args())
    src_dir = args['src_dir'][0]
    des_dir = args['des_dir'][0]
    backup(src_dir, des_dir)

if __name__ == '__main__':
    main()



