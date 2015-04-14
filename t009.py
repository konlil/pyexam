g = 9.8

class Gravity(object):
	def get(self, m):
		return m * g

obj = Gravity()
print obj.get(2)