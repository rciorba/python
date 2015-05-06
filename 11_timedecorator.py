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
	
foo1(1, 2)
foo2(1, 2, 3)