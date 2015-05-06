def sumNumbers():
	sum = 0
	file = open("d:/python/sum.txt", "r")
	for line in file:
		try:
			i = int(line)
			sum += i
		except:
			print "exc ", line
	return sum
			
print sumNumbers()