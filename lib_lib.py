# coding:utf-8

def do_in_echo():
	print 'before be override by lambda'

class mylib:
	def test(self, data):
		print self, data, 'origin class method'
		# return 1

# as global container
c = []
