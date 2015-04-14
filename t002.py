class FooIterator(object):
	def __init__(self, csv):
		self._csv = csv
		self._curr = 0
		
	def next(self):
		if self._curr >= len(self._csv):
			raise StopIteration
		else:
			res = self._csv[self._curr]
			self._curr += 1
			return res

class Foo(object):
	def __init__(self):
		self._list = [1, 2, 3, 4, 5]
		
	def __iter__(self):
		return FooIterator(self)
		
	def __len__(self):
		return len(self._list)
		
	def __getitem__(self, index):
		return self._list[index]
		
a = Foo()
for a1 in a:
	for b1 in a:
		print (a1, b1)