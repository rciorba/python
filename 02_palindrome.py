import math
	
def isPalindrome(number):
	rev = 0
	rmd = 0
	num = number
	while(num > 0): 
		rmd = num % 10; 
		rev = rev * 10 + rmd; 
		num = num / 10; 
	return rev == number 
         
def allPalindromesLowerThan(number):
	for i in range(number):
		if isPalindrome(i):
			print str(i) + " is a palindrome"
			
def allPalindromesLowerThan2ndVariant(number):
	print filter(isPalindrome, range(number))

def usingGenerator(n):
		x = 0
		while (True):
			if x > n:
				raise StopIteration()
			if isPalindrome(x):
				yield x 
			x += 1
			
class PalindromeFinder(object):
	def __init__(self, number):
		self.number = number
		self.x = 0
		
	def __iter__(self):
		while (True):
			if self.x > self.number:
				raise StopIteration
			if isPalindrome(self.x):
				yield self.x 
			self.x += 1
			
number = input("Number")
print [x for x in usingGenerator(number)]
gen = iter(PalindromeFinder(number))
print [x for x in PalindromeFinder(number)]


