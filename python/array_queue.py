class ArrayQueue:

	DEFAULT_CAPACITY = 10

	def __init__(self):
		self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0
	
	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise EMPTY('QUEUE IS EMPTY')
		return self._data[self._front]

	def dequeue(self):
		if self.is_empty():
			raise EMPTY('QUEUE IS EMPTY')
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		return answer  

	def enqueue(self, item):
		if self._size == len(self._data):
			self.resize(2 * len(self._data))
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = item
		self._size += 1

	def resize(self, cap):
		old = self._data
		self._data = [None]*cap
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front = 0

class Empty(Exception):
	pass

if __name__ == '__main__':
	Q = ArrayQueue()
	print("Queue Empty: {empty}".format(empty=Q.is_empty()))
	Q.enqueue("1")
	Q.enqueue("2")
	print("Length of Queue: {len}".format(len=len(Q)))
	print("First of Queue: {}".format(Q.first()))
	Q.dequeue()
	print("Length of Queue: {len}".format(len=len(Q)))
	print("First of Queue: {top}".format(top=Q.first()))
	Q.dequeue()
	print("Queue Empty: {empty}".format(empty=Q.is_empty()))