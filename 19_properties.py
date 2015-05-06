import os.path
import time
from threading import Timer

class Types(object):
	string = 1
	int = 2

class ReaderModes(object):
	simple = 1
	selfReading = 2
	
class PropertyException(BaseException):
	def __init__(self, txt):
		self.text = txt
	
	def __str__(self):
		return self.text
		
class Property(object):
	def __init__(self, _type, _key, _value):
		self.key = _key
		self.value = _value
		self.type = _type
		self.validateProperty()
		
	def validateProperty(self):
		if(self.type == Types.int):
			try:
				self.value = int(self.value)
			except:
				raise PropertyException("value " + self.value + " is not an int")
		#for string nothing is needed right now	

	def __str__(self):
		return "Property(key={0} value={1} type={2})".format(self.key, self.value, self.type)
		
	def __repr__(self):
		return self.__str__()
		
class AbstractPropertyReader(object):
	def __init__(self, _file, _separator):
		self.file = _file
		self.separator = _separator
		self.properties = []
		self.readProperties()
		
	def validateLine(self, line):
		import re
		matcher = re.compile("(int|string)"+ self.separator + "\w+" + self.separator + "\w+")
		if(not matcher.match(line)):
			raise PropertyException("property line is incorrectly formatted")
		
	def readProperties(self):
		raise NotImplementedError("Abstract method")
		
	def readLines(self):
		lines = []
		for line in open(self.file):
			lines.append(line)
		return lines
	
	def extractElements(self, line):
		elements = line.split(self.separator)
		return elements
		
	def __getitem__(self, index):
		return self.properties[index]
	
class SimplePropertyReader(AbstractPropertyReader):
	def __init__(self, _file, _separator):
		return super(SimplePropertyReader, self).__init__(_file, _separator)
		
	def readProperties(self):
		lines = self.readLines()
		for line in lines:
			self.validateLine(line)
			elements = self.extractElements(line)
			self.properties.append(Property(elements[0], elements[1], elements[2]))
		
class NotifyingPropertyReader(SimplePropertyReader):
	def __init__(self, _file, _separator, startAsDaemon = False):
		super(NotifyingPropertyReader, self).__init__(_file, _separator)
		self.listeners = []
		self.startAsDaemon = startAsDaemon
		self.lastModifiedDate = os.path.getmtime(self.file)
		self.startWatcher()
		
	def startWatcher(self):
		self.timer = Timer(1, self.determineIfPropertyHasChanged)
		self.timer.setDaemon(self.startAsDaemon)
		self.timer.start()
		
	def addListener(self, propertyChangedListener):
		self.listeners.append(propertyChangedListener)
		
	def removeListener(self, propertyChangedListener):
		self.listeners.remove(propertyChangedListener)
	
	def notifyListeners(self):
		print "notifying listeners"
		map(lambda x : x(self.properties), self.listeners)
		
	def determineIfPropertyHasChanged(self):
		print "timer has fired"
		if self.lastModifiedDate != os.path.getmtime(self.file):
			self.readProperties()
			self.notifyListeners()
			self.lastModifiedDate = os.path.getmtime(self.file)
		self.startWatcher()
	
class PropertyReaderFactory(object):
	@staticmethod
	def getReader(_file, _separator, _mode):
		if(_mode == ReaderModes.simple):
			return SimplePropertyReader(_file, _separator)
		elif(_mode == ReaderModes.selfReading):
			return NotifyingPropertyReader(_file, _separator)
				
				
def propertyModifed(properties):
	print "property file has been modified"
	print properties
	
class PropertyModifiedListener(object):
	def __call__(self, properties):
		print "Listener from class : property file has been modified"
		print properties
	
#listener adding vs timer starting race condition ignored
#also ignoring the fact that NotifyingReader is not threadsafe
reader = PropertyReaderFactory().getReader("property.txt", ":", ReaderModes.selfReading)
reader.addListener(propertyModifed)
reader.addListener(PropertyModifiedListener())
reader.removeListener(propertyModifed)
#time.sleep(200)
	
	
	
	
	