#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

print("Find pair strings with \"DocumentRoot\" and change it")
os.system("ruby list.rb")
a = input()

if a == 1:
    os.system("apt install nano && nano /data/data/com.termux/files/usr/etc/apache2/httpd.conf")
elif a == 2:
    os.system("apt install micro && micro /data/data/com.termux/files/usr/etc/apache2/httpd.conf")
elif a == 3:
    os.system("apt install joe && joe /data/data/com.termux/files/usr/etc/apache2/httpd.conf")
elif a == 4:
    os.system("apt install vim && vim /data/data/com.termux/files/usr/etc/apache2/httpd.conf")
elif a == 5:
    os.system("apt install emacs && emacs /data/data/com.termux/fi    les/usr/etc/apache2/httpd.conf")
elif a == 6:
    os.system("apt install neovim && nvim /data/data/com.termux/fi    les/usr/etc/apache2/httpd.conf")