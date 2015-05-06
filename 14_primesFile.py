from a_03_prime import *

def readFile():
	file = open('primes.txt')
	for line in file:
		print "Primes lower than ", line, " are ", primesLowerThan2(int(line))

def readFile2():
	return {int(x):primesLowerThan(int(x)) for x in open('primes.txt')}
		
#readFile()
print readFile2()
