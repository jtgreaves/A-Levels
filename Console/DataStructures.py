class Stack: 
	def __init__(self, size): 
		self.data = [None for n in range(size)] 
		self.initialSize = size
		self.maxSize = size
		self.top = -1 
	
	def push(self, value): 
		if self.top == self.maxSize - 1: 
			print("Stack was full, doubling size") 
			
			temp = self.data
			self.data = temp + [None for n in range(self.maxSize)]
			self.maxSize *= 2

		 
		self.top += 1 
		self.data[self.top] = value
	
	def pop(self): 
		if self.top == -1:
			print("Error - Stack is empty") 
			return False
		else: 
			temp = self.data[self.top]
			self.top -= 1
			return temp
		
	def output(self): 
		print(self.data)
		return self.data[self.top] 
		
class ShiftingQueue: 
	def __init__ (self, size): 
		self.data = [None for n in range(size)]
		self.size = size
		self.front = 0
		self.rear = 0 
			
	def add(self, value):
		if self.rear >= self.size:
			print("Queue is full!")
			if self.front != 0: 
				print("Shifting")
				self.shift()
			else: 
				print("Failed to shift")
				return False
			
		self.data[self.rear] = value
		self.rear += 1 		
		
	def remove(self):
		temp = self.data[self.front] 
		self.front += 1 
		return temp
	
	def shift(self): 
		temp = [None for n in range(self.size)] 
		
		pos = self.front
		index = 0
		while pos < self.rear: 
			temp[index] = self.data[pos]				
			pos += 1 
			index += 1 
						
		self.data = temp 
		self.rear = self.rear - self.front
		self.front = 0			
	
	def output(self): 
		print(self.data)

class CircularQueue: 
	def __init__ (self, size): 
		self.data = [None for n in range(size)]
		self.size = size
		self.front = 0
		self.rear = -1
			
	def add(self, value):
		if self.rear == -1: 
			self.data[0] = value 
			self.rear = 1
			
			return 
		elif self.rear == self.front: 
			print("Circular queue full!")
			return False 
		elif self.rear >= self.size:
			if self.front != 0: self.rear = 0 
			else: 
				print("Unable to become circular!") 
				return False 
			
		self.data[self.rear] = value
		self.rear += 1 		
		
	def remove(self):
		if self.front >= self.size: 
			self.front = 0 
			
		temp = self.data[self.front] 
		self.data[self.front] = None
		self.front += 1 
		return temp			
	
	def output(self): 
		print(self.data)

queue = CircularQueue(5)
while True: 
	queue.add(input("value: "))
	queue.output()
	queue.add(input("value: "))
	queue.output()
	print(queue.remove())
	queue.output()
	
	
		
