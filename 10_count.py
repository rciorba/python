
def count():
	i = 0
	while True:
		yield i
		i += 1
		
c = count().next;		

print c(), c(), c()
