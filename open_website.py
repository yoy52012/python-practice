# -*- coding: utf-8 -*-

# Script Name   : open_website.py
# Author        : chao yuan
# Created       : 17th January 2017
# Last Modified : 17th January 2017

# Description   : This srcipt will open the webbrowser with a given url(通过ssh连接获取远程服务器的信息)

import sys
import webbrowser

try:
    url = sys.argv[1]
    webbrowser.open(url)
except IndexError:
    print("Please input a url")
