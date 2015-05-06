import dis
import sys
from cStringIO import StringIO

class LoggerDecorator(object):
	#attempt to decorate all function from a specific class
	def __init__(self, cls):
		self.cls = cls

	def investigate(self):
		for k, v in self.cls.__dict__.iteritems():
			if hasattr(v, "__call__"):
				print "function found ", v.__name__
				#clearly not doing what is supposed to do 
				v = LoggerDecorator.decorate(v)
		
	@staticmethod
	def decorate(function):
		function = LoggerDecorator.decorator(function)
	
	@staticmethod
	def decorator(function):
		def inner(function):
			print "I am calling ", function.__name__
			return function()
		return inner
		
class Test(object):
	def __init__(self):
		print "cucu"
		
	def pa(self):
		print "ducu"
		
LoggerDecorator(Test).investigate()
Test().pa()