class CSV(object):
	def __init__(self):
		self._list = []
		
	def push(self, item):
		self._list = item
		
	def set(self, index, item):
		self._list[index] = item
		
	def show(self):
		print self._list
		
a = CSV()
item1 = [1, 2, 3]
a.push(item1)
a.show()
item1[1] = 4
a.show()
