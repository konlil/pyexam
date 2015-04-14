class Foo(object):
	def __init__(self):
		self._list = [1, 2, 3, 4, 5]
		
	def __iter__(self):
		counter = [0]
		
		def get():
			if counter[0] >= len(self._list):
				return None
				
			res = self._list[counter[0]]
			counter[0] += 1
			return res
			
		return iter(get, None)
		
a = Foo()
for a1 in a:
	for b1 in a:
		print (a1, b1)
		
#itr = iter(a)
#print itr