class Foo(object):
	def __init__(self):
		self._list = [1, 2, 3, 4, 5]
		
	def __iter__(self):
		ii = iter(self._list)
		#print 'get foo iterator:', ii
		return ii
		
a = Foo()
for a1 in a:
	for b1 in a:
		print (a1, b1)
		
itr = iter(a)
print itr
