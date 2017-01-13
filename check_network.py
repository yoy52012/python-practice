# -*- coding: utf-8 -*-

# Script Name   : file_rename.py
# Author        : chao yuan
# Created       : 12th January 2017
# Last Modified : 13th January 2017

import urllib.request
import urllib.error
try:
    request = urllib.request.urlopen('http://www.baidu.com', timeout=2)
    if request.getcode() == 200:
        print("Connection is ok!")
except urllib.error.URLError:
    print("No internet connection")

