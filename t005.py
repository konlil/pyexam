# constant
MaxCount = 10*7

f = open(r'c:\1.txt', 'wt')
for x in xrange(MaxCount):
	print >> f, x
f.close()
