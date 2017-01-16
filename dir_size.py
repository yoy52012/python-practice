# -*- coding: utf-8 -*-

# Script Name   : dir_size.py
# Author        : chao yuan
# Created       : 16th January 2017
# Last Modified : 16th January 2017

# Description   ：This will get the total size of a given folder

import os
import sys

def main():
    '''
    Call the main method
    '''
    try:
        path = sys.argv[1]
        if os.path.exists(path):
            fsize = {
                'Bytes': 1,
                'Kilobytes': float(1) / 1024,
                'Megabytes': float(1) / (1024 * 1024),
                'Gigabytes': float(1) / (1024 * 1024 * 1024)
            }
            dir_size = 0
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    dir_size += os.path.getsize(os.path.join(dirpath, filename))

            fsize_list = [str(round(fsize[key] * dir_size, 2))  + "" + key for key in fsize]
            for res in sorted(fsize_list)[::-1]:
                print("Folder Size : "+res)
        else:
            print('The given path does not exist.')
    except IndexError:
        sys.exit("Please provide a path argument.")
    

if __name__ == '__main__':
    main()
    