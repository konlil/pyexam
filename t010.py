class A(object):
	def fox(self):
		print 'fox'
		
def dog(self):
	print 'dog'
	
def cat(self):
	print 'cat'
	
def duck(self):
	print 'duck'
	
a1 = A()
a2 = A()
a1.fox()
a2.fox()
print '-' * 30

A.fox = dog
a1.fox()
a2.fox()
print '-' * 30

import new
a2.fox = new.instancemethod(cat, a2, A)
a1.fox()
a2.fox()
print '-' * 30

print dir(a1)
print dir(a2)
print '-' * 30

A.fox = duck
a1.fox()
a2.fox()
print '-' * 30

print a1.__dict__
print a2.__dict__
print '-' * 30

del a2.__dict__['fox']
a1.fox()
a2.fox()
print '-' * 30