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

# override build-in module
import time

print time.time()

# make _time as build-in method, or it will in for-loop forever,
# copy 一份到 local memory, 待會整合奧用
from time import time as _time

def time2():
	# 這樣會變成無窮遞迴, 因為已經被替換掉了
	
	# return 'after override: ' + str(time.time())
	return 'after override build-in Module: ' + str(_time()) + ' end!'

time.time = lambda: time2()

print time.time()
