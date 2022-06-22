class JobNode: 
	def __init__ (self, name, time): 
		self.name = name # String 
		self.time = time # In seconds 
		

class CircularQueue: 
	def __init__ (self, size): 
		self.data = [None for n in range(size)]
		self.size = size
		self.front = 0
		self.rear = -1
			
	def add(self, value):
		if self.rear == -1: # If the queue is empty 
			self.data[0] = value 
			self.rear = 1
			return 
		if not self.circulate: return 
			
		# If it is able to add to the queue 
		temp = self.data
		nodeNumber = 0 
		placeFound = False 
		while nodeNumber < len(self.data): 
			if self.data[nodeNumber] != None and value != None:
				if value.time < self.data[nodeNumber].time and not placeFound: # Those with the lowest time go first 
					placeFound = True 
					temp[nodeNumber] = value
				
				elif placeFound:
					if (nodeNumber + 1) == len(self.data):
						if not self.circulate: return
						temp[0] = self.data[nodeNumber] 
					else:
						if not self.circulate: return
						temp[nodeNumber + 1] = self.data[nodeNumber] 
				
			nodeNumber += 1   
			
		if not placeFound: self.data[self.rear] = value
		else: self.data = temp
		 
		self.rear += 1 		
	
	def circulate(self):
		if self.rear == self.front: # If the queue is full 
			print("Circular queue full!")
			return False 
			
		elif self.rear >= self.size: # If the person has not removed any
			if self.front != 0: self.rear = 0 
			else: 
				print("Unable to become circular!") 
				return False 
		return True
				
	def remove(self):
		if self.front >= self.size: 
			self.front = 0 
			
		temp = self.data[self.front] 
		self.data[self.front] = None
		self.front += 1 
		return temp			
	
	def output(self): 
		for x in self.data: 
			if x != None: 
				print(x.time)

queue = CircularQueue(5)
while True: 
	queue.add(JobNode("1", int(input("value: "))))
	queue.output()
	queue.add(JobNode("1", int(input("value: "))))
	queue.output()
	queue.add(JobNode("1", int(input("value: "))))
	queue.output()
	queue.add(JobNode("1", int(input("value: "))))
	queue.output()
	queue.remove()
	
	
		
