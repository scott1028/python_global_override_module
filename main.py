# coding:utf-8
# Python Override Existed Module Method, monkey patch...
# This action must in main.py

import lib_lib

def echo2():
	print 'after be override by lambda'

from lib import echo

echo()

# 就可以 Override Global 的 Module Method
lib_lib.do_in_echo = lambda: echo2()

from lib import echo

echo()
