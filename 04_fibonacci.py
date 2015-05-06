def fib_iter(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
	
def fib_rec(nn):
	if nn == 0 or nn == 1:
		return 1
	return fib_rec(nn - 1) + fib_rec(nn - 2)
	
def all_fib_numbers_under(n, function = fib_iter):
	fib_numbers = []
	for i in range(n):
		fib_numbers.append(function(i))
	return fib_numbers
		
def all_fib_numbers_under2(n, function = fib_iter):
	fib_numbers = []
	return map(function, range(n))
	
n = input("Number ")
print all_fib_numbers_under2(n, fib_rec)