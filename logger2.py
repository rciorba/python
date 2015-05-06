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
				v = decorate(v)
				

class Test(object):
	def __init__(self):
		print "cucu"
		
	def pa(self):
		print "ducu"
		
LoggerDecorator(Test).investigate()

	