class BinHeap:
	"""
	A complete tree can be represented using a list where a node at 
	location i has its children at positions 2i and 2i + 1. Nodes are  
	layed out Breadth First 
	"""
	def __init__(self):
		self.heapList = []
		self.currentSize = 0

	def percUp(self,i): #percLeft if you lay out everything in a list
		while i // 2 > 0: #just division by 2 followed by floor
			if self.heapList[i] < self.heapList[i // 2]: #comparison with parent
				self.heapList[i // 2],self.heapList[i] = self.heapList[i],self.heapList[i // 2]
			i = i // 2

	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percDown(self,i): #percRight if you lay out everything in a list
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				self.heapList[i] , self.heapList[mc]  = self.heapList[mc] , self.heaplist[i]
			i = mc

	def minChild(self,i):
		#boundary condition 
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			#pick the smallest of the two children
			if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heaplist[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heaplist.pop()
		self.percdown(1)
		return retval

	def buildHeap(self,alist):
		"""
		Batch build heap in O(N) instead of usual O(N log N) cost
		"""
	    i = len(alist) // 2
    	self.currentSize = len(alist)
    	self.heapList = [0] + alist[:]
   	 	while (i > 0):
        	self.percDown(i)
        	i = i - 1



