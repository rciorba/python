from collections import deque

class BasicQueueException(BaseException):
	def __init__(self, text):
		self.text = text
	
	def __str__(self):
		return self.text
		
class QueueEmptyException(BasicQueueException):
	def __init__(self):
		super(QueueEmptyException, self).__init__("Queue is Empty")

class Queue(object):
	def __init__(self):
		self.storage =  deque([])
		self.currentIndex = 0
		
	def __str__(self):
		return "Queue at " + str(id(self)) + " : "+ str(self.storage)
		
	def __eq__(self, that):
		if that is None:
			return false
		if not isInstance(that, Queue):
			return false;
		if id(self) == id(that):
			return true
		return self.storage == that.storage
		
	def __getitem__(self, index):
		if(len(self.storage) - 1 < index):
			raise IndexError, StopIteration
			return None
		else:
			return self.storage[index]
		
	def __setitem__(self, index, value):
		if(len(self.storage) - 1 < index):
			print "Index out of bounds - use enqueue"
		else:
			self.storage[index] = value
	
	def __len__(self):
		return self.storage.__len__()
	
#	def __iter__(self):
#		return self
		
#	def next(self): # weird is not __next__
#		if(self.currentIndex >= len(self)):
#			raise StopIteration()
#		self.currentIndex += 1
#		return self[self.currentIndex - 1]
	
	def enqueue(self, item):
		self.storage.append(item)
		return self
	
	def dequeue(self):
		if(len(self.storage) == 0):
			raise QueueEmptyException()
		return self.storage.popleft()

q = Queue().enqueue(1).enqueue(3).enqueue(4)
print q.dequeue()
print q
print map(lambda x : x + 1, q)



	

