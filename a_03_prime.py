from itertools import *

def isPrime(n):
	for i in range(2, n - 1):
		if n % i == 0:
			return False
	return True
	
def primesLowerThan(n):
	foundPrimes = []
	for i in range(1, n):
		if isPrime(i):
			foundPrimes.append(i)
	return foundPrimes
			
def primesLowerThan2(n):
	return [x for x in ifilter(isPrime, xrange(1, n))]

if __name__ == "__main__":
	n = input("Number ")
	print primesLowerThan2(n)
#print  isPrime2ndVariant(n)

