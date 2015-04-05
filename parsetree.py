import Stack
import BinaryTree

def buildParseTree(fpexp):
	fplist = fpexp.split()
	pStack = Stack
	eTree  = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	for i in fplist:
		if i == '(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
	
		elif i not in ['+','-','*','/',')']:
			currentTree.setRootVal(int(i))
			parent = pStack.pop()
			currentTree = parent
		elif i in ['+','-','*','/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i in ['+','-','*','/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()

		elif i == ')':
			currentTree = pStack.pop()
		else:
			raise ValueError
	return eTree

def evaluate(parseTree):
	opers = {'+':operator.add,'-':operator.sub,'*':operator.mul, '/':operator.truediv}

	leftC  = parseTree.getLeftChild()
	RightC = parseTree.getRightChild()

	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC),evaluate(rightC))

if __name__ == "__main__":
	pt = buildParseTree("( ( 10 + 5 ) * 3 )")
	assert(evaluate(pt) == 45)