
# -*- coding: utf-8 -*-

# Script Name   : file_rename.py
# Author        : chao yuan
# Created       : 10th January 2017
# Last Modified : 11th January 2017


import os
import argparse

def batch_rename(work_dir, old_extension, new_extension):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    ( 将指定目录中指定后缀的文件重命名为新的后缀 )
    '''
    for filename in os.listdir(work_dir):                    # traverse all the files in the givern directory 遍历指定目录下所有的文
        file_extension = os.path.splitext(filename)[1]       # get file's current extension
        if file_extension == old_extension:
            new_file = filename.replace(file_extension, new_extension) # replace the old extension with the new extension
            os.replace(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, new_file)
            )                                                   # rename the file

def get_parser():
    '''
    get command line arguments
    (获取命令行参数)
    '''
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser

def main():
    '''
    Call the main method
    '''
    parser = get_parser()
    args = vars(parser.parse_args())

    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    new_ext = args['new_ext'][0]

    batch_rename(work_dir, old_ext, new_ext)

if __name__ == '__main__':
    main()


