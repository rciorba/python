class LoggerException(BaseException):
	def __init__(self, msg):
		pass

class One(object):
	def __str__(self):
		return " !! one !! "
		
class LogItem(object):
	def __init__(self, text):
		self.root = text
		
	@staticmethod
	def isLoggable(potentialLoggable):
		return hasattr(potentialLoggable, "__str__")
		
	def __add__(self, loggable):
		if not LogItem.isLoggable(loggable):
			raise LoggerException("Not loggable")
		self.root += loggable.__str__()		
		return self
	
	def __repr__(self):
		return self.root
	
	def __str__(self):
		return self.__repr__()
		
class Logger(object):
	def __init__(self, string):
		logItem = eval("LogItem('') + " + string)
		print logItem.root
		
Logger('"mama" + "corina" + "tata" + 1')
"mama are {} mere".format(2)
Logger('1 + LogItem("mama") + One() + 2345')

print 1, LogItem("mama"), One(), 2345
