# -*- coding: utf-8 -*-

# Script Name   : check_files.py
# Author        : chao yuan
# Created       : 11th January 2017
# Last Modified : 13th January 2017

# Description   : check the given file  exists and whether we can read or not (检查所给文件是否存在且是否可以打开并读取)

import os
import sys

def usage():
    '''
    Tell the user how to use this script.
    '''
    print('[-] Usage: python check_file.py <filename1> [filename2] ... [filenameN]')
    exit(0)

def main():
    '''
    Call the main method.
    '''
    if len(sys.argv) >= 2:
        filenames = sys.argv[1:]
        for filename in filenames:
            if os.path.isfile(filename):
                if  not os.access(filename, os.R_OK):
                    print('[-] ' + filename + 'access denied.')
                    filenames.remove(filename)
            else:
                print('[-] ' + filename + ' does not exist.')
                filenames.remove(filename)

        for filename in filenames:
            print('[+] ' + filename + ' can be opened and read.')
    else:
        usage()

if __name__ == '__main__':
    main()
