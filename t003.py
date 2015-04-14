class Foo(object):
	def __init__(self):
		self._list = [1, 2, 3, 4, 5]
		
	def __iter__(self):
		for v in self._list:
			yield v
		
a = Foo()
for a1 in a:
	for b1 in a:
		print (a1, b1)
		
#itr = iter(a)
#print itr
