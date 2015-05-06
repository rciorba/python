def filter(func, iterable):
	result = []
	for i in iterable:
		if func(i) == True:
			result.append(i)
	return result
	
def lazyFilter(func, iterable):
	for i in iterable:
		if func(i):
			yield i
			
for x in lazyFilter(lambda x : x > 2, [1, 2, 1, 2, 3, 4]):
	print x