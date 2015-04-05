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
				currentNode.LeftChild = TreeNode(key,val,parent=currentNode)
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

class TreeNode:
	def __init__(self,key,val,left = None,right = None,parent = None):
		self.key       = key
		self.value     = val
		self.leftChild = left
		self.righChild = right
		self.parent    = parent

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
		self.rightChild = righChild

		if self.hasLeftChild():
			self.leftChild.parent = self

		if self.hasRightChild():
			self.righChild.parent = self 


