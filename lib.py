# coding:utf-8

import lib_lib

def echo():
	lib_lib.do_in_echo()

def echo3():
	lib_lib.mylib().test(123)

# test not existed member access
def echoX():
	try:
		print lib_lib.c
	except Exception as e:
		print e
