import gc
import weakref

class A(object):
	def __init__(self):
		#pass
		
		#self.a = weakref.ref(self) #it clears them
		self.a = self # it does not clear them independent whether a __del__ is there or not
		
#	def __del__(self):
#		print "del called on ", id(self)
	
	
def f():		
	a = A()
	print a.__dict__
	print "I have an A at ", hex(id(a)).upper(), " with dict at ", hex(id(a.__dict__)).upper()
	
f()
gc.set_debug(gc.DEBUG_LEAK)
# The number of unreachable objects found is returned.
print gc.collect()
