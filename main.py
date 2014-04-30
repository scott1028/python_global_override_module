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

from lib import echo, echo3

echo()

echo3()

def _echo3(self, data):
	print self, data, 'after override class method'

# override instance method!
lib_lib.mylib.test = lambda self, data: _echo3(self, data)
echo3()

# test import as local function
from lib_lib import mylib
mylib().test(789)  # as same as after override instance method

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


# 動態新增 class 方法
class Aa: pass
Aa.test = lambda self: 100
print Aa().test()  # return 100

# 定義 getter
class Aaa:
	@property
	def a(self):
		return 555
print Aaa().a		# as perperty, 使用 getter 當作 property

class Bb:
	@property
	def a(self):
		return 123

# make access control
# 實現 getter 跟 setter 的做法
class C(object):
    def __init__(self):
        self._x = 0

    def getx(self):
        return self._x + 10000

    def setx(self, value):
    	print 'setter: set self._x'
        self._x = value

    def delx(self):
        del self._x

    @property
    def y(self):
    	return 555

    # 一行來實現 x 的 getter 跟 setter
    x = property(getx, setx, delx, "I'm the 'x' property.")

cc = C()

# __slots__ 應用(Python 本來是 Dynamical Member, 使用 __slots__ 設定後可以加快執行速度, 但是就不能任意增加屬性了)
# 並且將既有定義的屬性變為 Read-Only
class Foo3(object):
	__slots__ = ('x')

try:
	Foo3().y = 3123
except Exception as e:
	print e

#
# 如果你想要控制可以指定給物件的特性名稱，則可以在類別上定義__slots__特性，
# 該特性是一個字串清單，列出可指定給物件的特性名稱。
# 可以利用定義 __slot__ 加上定義屬性來製作 read-only 成員(property, instance method 等)
#
# ref: http://openhome.cc/Gossip/Python/Slots.html
class MyClass( object ) :
   	# 使用 __slots__ = () 讓 instance 後的 Property 變為 Read-Only
    __slots__ = ('m', 'x')  #( 'm' )
    
    m = None  # read-only, 因為 __slots__ 將既有屬性改為 read-only, 所以即使上面有加入 __slots__('m') 也一樣

    bb = 0
    test3 = 10

    def test2(self):
    	print 888

aaa = MyClass() # create one
MyClass.test1=lambda self: 312
MyClass.test2=lambda self: 752
try:
	aaa.m = "set m value"
except Exception as e:
	print e

try:
	aaa.test2 = lambda self: 999
except Exception as e:
	print e

try:
	aaa.test3 = lambda self: 999
except Exception as e:
	print e

aaa.x=1000
aaa.x=200
print aaa.x, 'because "aaa.x" in the __slots__ and not defined in class.'
