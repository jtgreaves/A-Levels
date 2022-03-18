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
		
myStack = Stack(2)

myStack.push("Test") 
myStack.push("Example") 
myStack.push("Woo") 
myStack.push("Test") 
myStack.push("Example") 
myStack.push("Woo") 
myStack.push("Test") 
myStack.push("Example") 
myStack.push("Woo") 

print(myStack.output())

			
	
		
