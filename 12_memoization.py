def memoize(f):
    existingResults = {}
    def inner(n): #again closures
		if n not in existingResults:            
			existingResults[n] = f(n)
			print n, " not found in cache"
		print n, " found in cache"
		return existingResults[n]
    return inner
    
@memoize
def fib(n):
    if n == 0 or n == 1:
		return 0
    return fib(n - 1) + fib(n - 2)

fib(3)
fib(3)

