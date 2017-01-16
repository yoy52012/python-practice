# -*- coding: utf-8 -*-

# Script Name   : file_info.py
# Author        : chao yuan
# Created       : 16th January 2017
# Last Modified : 16th January 2017

# Description   ：Get the information of given file

import os
import stat
import time
import sys

def get_human_size(file_size):
    '''
    Get the size of file in a comprehensiable way
    '''
    if 0 <= file_size < 2**10:
        print("{}B".format(file_size))
    elif 2**10 <= file_size < 2**20:
        print("{:.2f}KB".format(file_size/(2**10)))
    elif 2**20 <= file_size < 2**30:
        print("{:.2f}MB".format(file_size/(2**20)))
    else:
        print("{:.2f}GB".format(file_size/(2**30)))

def get_file_info(file_path):
    '''
    Get and Print file's infomation
    '''
    try:
        file_stat = os.stat(file_path)
        if stat.S_ISDIR(file_stat[stat.ST_MODE]):
            print("This a directory")
        else:
            file_info = {
                'file_size' : file_stat[stat.ST_SIZE],
                'file_ct'   : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat[stat.ST_CTIME])),
                'file_at'   : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat[stat.ST_ATIME])),
                'file_mt'   : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat[stat.ST_MTIME]))
            }
            print("file name = %s " % os.path.basename(file_path))
            print("file size = ", end='')
            get_human_size(file_info['file_size'])
            print("file CreatTime = {[file_ct]}".format(file_info))
            print("file AccessTime = {[file_at]}".format(file_info))
            print("file ModifyTime = {[file_mt]}".format(file_info))

    except OSError:
        print('\nNameError : [%s] No such file or directory\n', file_path)


def main():
    '''
    Call the main method.
    '''
    try:
        path = sys.argv[1]
        if os.path.exists(path):
            get_file_info(path)
        else:
            print('The given path does not exist.')
    except IndexError:
        sys.exit("Please provide an argument.")

if __name__ == '__main__':
    main()



