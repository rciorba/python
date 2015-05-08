import time
getCurrentTimeMillis = lambda: int(round(time.time() * 1000))

def uberLogTimes():
	globalTime = {'time' : 0}
	def logTimes(func):
		def inner(*args, **argss): 
			then = getCurrentTimeMillis() 
			return_ = func(*args, **argss)
			
			duration = getCurrentTimeMillis() - then
			globalTime['time'] += duration
			
			print func.func_name + " call duration was " , duration
			print "Total time " , globalTime['time']
			return return_
		return inner
	return logTimes

# you don't really pass any arguments to this decorator factory
# can you get rid of it entirely?
logger = uberLogTimes()

@logger
def foo1(mama, tata = 1):
	print "inside foo1"
	time.sleep(2)
	return 234
	
@logger
def foo2(mama, tata, corina):
	print "inside foo2"
	time.sleep(3)
	return "mama"

@logger
def foo3():
	time.sleep(4)
	assert False
	
foo1(1, 2)
foo2(1, 2, 3)
foo3() # how about this one?
