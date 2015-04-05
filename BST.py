class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def puts(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			#if no root exists then just make the new node root
			self.root = TreeNode(key,val)
		self.size = self.size + 1

	def _put(self,key,val,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild = TreeNode(key,val,parent=currentNode)
		elif key > currentNode.key:
			if currentNode.hasRightChild():
				self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key,val,parent=currentNode)
		else:
			#replace key value and keep everything else the same
			currentNode.replaceNodeData(key,val,currentNode.leftChild,currentNode.rightChild)


	#override [] operator for assignment so can do things like
	#MyTree['imakey'] = imavalue
	#same thing applies to get
	def __setitem__:
		self.put(k,v)


	def get(self,key):
		if self.root:
			res = self._get(key,self.root)
			if res:
				return res.value
		else:
			return None

	def _get(self,key,currentNode):
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif key < currentNode.key:
			return self._get(key,currentNode.leftChild)
		else:
			return self._get(key,currentNod.rightChild)

	def __getitem__(self,key):
		return self.get(key)

	#overloads 'in' operator 
	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False

	def delete(self,key):
		if self.size > 1:
			nodeToRemove = self._get(key,self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size = self.size - 1
			else:
				raise KeyError("Error, key not in tree")
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size = self.size - 1
		else:
			raise KeyError("Error, key not in tree")
	
	#so you can delte by saying del TreeName[keyOfElementToDelete]
	def __delitem__(self,key):
		self.delete(key)

	def remove(self):
		if currentNode.isLeaf(): #leaf is the easiest
			if currentNode == currentNode.parent.leftChild:
				currentNode.parent.leftChild = None
			else:
				currentNode.parent.rightChild = None


		elif currentNode.hasBothChildren(): #interior node
			succ = currentNode.findSuccessor()
			succ.spliceOut()
			currentNode.key = succ.key
			currentNode.value = succ.value



		else: #node has just one child, promotion is easy
			if currentNode.hasLeftChild():
				if currentNode.isLeftChild():
					currentNode.leftChild.parent  = currentNode.parent
					currentNode.parent.leftChild  = currentNode.leftChild
				elif currentNode.isRightChild():
					currentNode.leftChild.parent  = currentNode.parent
					currentNode.parent.rightChild = currentNode.leftChild
				else:
					#if root is deleted the left node becomes the new root
					currentNode.replaceNodeData(currentNode.leftChild.key,
						currentNode.leftChild.value,currentNode.leftChild.leftChild
						currentNode.leftChild.rightChild)  
			else:
				if currentNode.isLeftChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.leftChild =  currentNode.rightChild
				elif currentNode.isRightChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.rightChild
				else:
					currentNode.replaceNodeData(currentNode.rightChild.key,
						currentNode.rightChild.value,
						currentNode.rightChild.leftChild,
						currentNode.rightChild.rightChild)



class TreeNode:
	def __init__(self,key,val,left = None,right = None,parent = None):
		self.key        = key
		self.value      = val
		self.leftChild  = left
		self.rightChild = right
		self.parent     = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.leftChild or self.rightChild)

	def hasAnyChildren(self):
		return self.leftChild or self.rightChild

	def hasBothChildren(self):
		return  self.leftChild and self.rightChild

	def replaceNodeData(self,key,value,leftchild,rightchild):
		self.key        = key 
		self.value      = value
		self.leftChild  = leftChild
		self.rightChild = rightChild

		if self.hasLeftChild():
			self.leftChild.parent = self

		if self.hasRightChild():
			self.rightChild.parent = self 

	def findMin(self):
		current = self
		while current.hasLeftChild():
			current = current.leftChild
		return current

	#in order traversal is default
	def __iter__(self):
		if self:
			if self.hasLeftChild:
				for elem in self.leftChild:
					yield elem
			yield self.key
			if self.hasRightChild():
				for elem in self.rightChild:
					yield elem
	
	#preorder traversal not exposed but possible to reimplement __iter__ here 
	def _preOrder(self):
		if self:
			yield self.key
			if self.hasLeftChild:
				for elem in self.leftChild:
					yield elem
			if self.hasRightChild():
				for elem in self.rightChild:
					yield elem

	def _postOrder(self):
		if self:
			if self.hasLeftChild:
				for elem in self.leftChild:
					yield elem
			if self.hasRightChild:
				for elem in self.rightChild:
					yield elem
			yield self.key


	def spliceOut(self):
		#to implement
		pass

	def findSuccessor(self):
		succ = None
		if self.hasRightChild:
			succ = self.rightChild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
					succ = self.parent
				else:
					#find succesor of parent ignoring current node
					self.parent.rightChild = None
					succ = self.parent.findSuccessor()
					self.parent.rightChild = self


if __name__ == "__main__":
	#testing it out
	print "This ain't your grandma's BST"
	aTree = BinarySearchTree()
	aTree[1] = "python"
	aTree[3] = "datastructures"
	aTree[6] = "are dope"

	aTree[1] = aTree[3]
	del aTree[3]
	for keys,vals in aTree:
		print("Key: %i Value: %s %(keys,vals)")

