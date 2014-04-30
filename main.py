# coding:utf-8
# Python Override Existed Module Method, monkey patch...
# This action must in main.py

import lib_lib

def echo2():
	print 'after be override by lambda'

from lib import echo

echo()

# 就可以 Override Global 的 Module Method, 路徑要完整
# 不能使用：
# 	from lib_lib import do_in_echo
#
# 	do_in_echo = lambda: echo2()
#
# 	這樣他不會改到那個 Module 的物件。只會改道 Local Function Ref, 只有在這個 Main 有效。

lib_lib.do_in_echo = lambda: echo2()

from lib import echo

echo()
