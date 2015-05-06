def map(func, iterable):
	result = []
	for i in iterable:
		result.append(func(i))
	return result

def filter(func, iterable):
	result = []
	for i in iterable:
		if func(i) == True:
			result.append(i)
	return result

def reduce(func, iterable, initializer):
	result = initializer
	for i in iterable:
		result = func(result, i) 
	return result
	
def withoutUsingMap(n):	
	sum = lambda x, y : x + y
	contraint = lambda x : x * (x - 1) % 3 == 0
	print reduce(sum, filter(contraint, range(1, n)), 0)
	
def usingAlsoMap(n):
#	:) not working
	sum = lambda x, y : x + y
	contraint = lambda x : x 
	mapper = lambda x : x * (x -1) % 3 == 0 
	print reduce(sum, filter(contraint, map(mapper, range(1, n))), 0)
	
withoutUsingMap(10)
	
#def sum():
#	s = [0]
#	def inner(x):
#		s[0] += x
#		return s
#	return inner
	
#print map(sum(), [1, 2, 3, 4])[-1]	
	
	
	
	
	
	


