class Foo(object):
	def __init__(self):
		self._list = [1, 2, 3, 4, 5]
		self._curr = 0
		
	def __iter__(self):
		self._curr = 0
		return self
		
	def next(self):
		if self._curr >= len(self._list):
			raise StopIteration
		else:
			res = self._list[self._curr]
			self._curr += 1
			return res
a = Foo()
#for a1 in a:
#	print a1

for a1 in a:
	for b1 in a:
		print (a1, b1)
