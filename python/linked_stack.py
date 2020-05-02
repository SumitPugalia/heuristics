class LinkedStack:
	class _Node:
		__slots__= '_element', '_next'
	
		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._size = 0
		self._head = None

	def __len__(self):
		return self._size
	
	def push(self, item):
		self._head = self._Node(item, self._head)
		self._size += 1

	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._head._element

	def is_empty(self):
		return self._size == 0

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty') 
		
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		return answer

class Empty(Exception):
	pass

if __name__ == '__main__':
	S = LinkedStack()
	print("Stack Empty: {empty}".format(empty=S.is_empty()))
	S.push("1")
	S.push("2")
	print("Length of Stack: {len}".format(len=len(S)))
	print("Top of Stack: {}".format(S.top()))
	S.pop()
	print("Length of Stack: {len}".format(len=len(S)))
	print("Top of Stack: {top}".format(top=S.top()))
	S.pop()
	print("Stack Empty: {empty}".format(empty=S.is_empty()))
