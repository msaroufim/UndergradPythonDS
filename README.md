# Python Undergrad DataStructures and Algo Implementations

Since people seem to care about this stuff, I've added implementations of
important undergrad algorithms in Python. I'm using [Problem Solving with Algorithms and Data Structures as a guide](http://interactivepython.org/runestone/static/pythonds/index.html). Open an issue if you'd like me to implement a specific one.

So far I have:

## The Basics

* Stacks (nothing too surprising)
```python
aStack = Stack()
aStack.push(5)
aStack.pop()
```
* Queues, more of the same
* Deques, do you really need me to implement those too?
* Min-heap: the code is much more easily understood if you take into account that a complete tree can be represented by a list where for an element at position ```i``` its children are at position ```2i``` and ```2i + 1```. Imagine spreading out all the elements of a tree Breadth First.
 

I should point out this [SO](http://stackoverflow.com/questions/9755721/build-heap-complexity) link. Textbooks generally state that building a heap is ```O(n log n)``` time which is correct if you are inserting the elements in a heap one by one. BUT if you just put all the elements in, in an arbitrary order and heapify then you can bring that cost down to ```O(N)```

```python
def buildHeap(self,alist):
        i = len(alist) // 2 #nodes in alist[:i] are all leaves
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:] #[0] at beginning helps arithmetic work
        while (i > 0):
            #every element will be pushed to the correct location after percdown
            self.percDown(i) 
            #do this for all non-leaf elements
            i = i - 1

myHeap = BinHeap()
a = [1,4,11,2,3,6,0]
myHeap.buildHeap(a)
```

## Sorting

* MergeSort
* QuickSort 
    - Elegant but inefficient filter based solution
    - Efficient in memory solution (in progress, needs a fix)

## Dynamic Programming
* Smallest amount of change problem: Suppose you had 1, 5, 10, and 25 cent coins what's the smallest number of coins you'd need to give me 63 cents in change. The greedy solution is optimal for the 1,5,10,25 values, if you add a 21 cent coin then the greedy solution will fail. So greedy won't work for a general case solution so we have 3 methods sorted in increasing awesomeness.

```python
#will need to use bigger lists to see effect irl
GetChangeInstance = GetChange()

#u slow m8
    print(GetChangeInstance.recMC([1,5,10,25,21],63))
    
    #better
    print(GetChangeInstance.recMCMemoized([1,5,10,25,21],63))

    #duuuude
    print(GetChangeInstance.DPMC([1,5,10,25,21],63))
```

## Trees

* Binary Search Tree with a gloriously simple API:

```python
aTree = BinarySearchTree()
    aTree[1] = "python"
    aTree[3] = "datastructures"
    aTree[6] = "are dope"

    aTree[1] = aTree[3]
    del aTree[3]
    for keys,vals in aTree:
        print("Key: %i Value: %s %(keys,vals)")
```

All Three different tree traversal algorithms, don't ever let this stuff confuse you again! Rename ```__iter__``` to ```_inorder``` and rename ```_postorder``` to ```__iter__``` to change the default inorder tree traversal when you iterate over the tree

```python
def _postOrder(self):
        if self:
            if self.hasLeftChild:
                for elem in self.leftChild:
                    yield elem
            if self.hasRightChild:
                for elem in self.rightChild:
                    yield elem
            yield self.key
```

## Graph Algorithms

* Graph Data Structure

* Depth First Search

```python
currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
```

* Replace the Queue by a stack!

