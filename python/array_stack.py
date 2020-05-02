class ArrayStack:

	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)
	
	def push(self, item):
		self._data.append(item)

	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]

	def is_empty(self):
		return len(self._data) == 0

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty') 
		return self._data.pop()

class Empty(Exception):
	pass

if __name__ == '__main__':
	S = ArrayStack()
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
