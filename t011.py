import sys
class A(object):
	def __init__(self):
		pass

	def show(self):
		print 'I am A'

a = A()
print isinstance(a, object)
print isinstance(A, object)
print isinstance(a.show, object)
print isinstance(A.__init__, object)
print isinstance(type(A), object)
print type(A)
print isinstance(type(type(A)), object)
print type(type(A))
print isinstance(a.show(), object)
print isinstance(sys, object)