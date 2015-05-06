
def map(func, iterable):
	result = []
	for i in iterable:
		result.append(func(i))
	return result
	
def mapLazy(func, iterable):
	for i in iterable:
		yield func(i)
		
my_inc = lambda x : x + 1
for i in mapLazy(my_inc, [1, 2, 3]):
	print i
	
