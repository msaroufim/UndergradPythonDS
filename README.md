# Python Undergrad DataStructures and Algo Implementations

Since people seem to care about this stuff, I've added implementations of
important undergrad algorithms in Python. I'm using [Problem Solving with Algorithms and Data Structures as a guide](http://interactivepython.org/runestone/static/pythonds/index.html) Open an issue if you'd like me to implement a specific one.

So far I have:

## Sorting

* MergeSort
* QuickSort 
    - Elegant but inefficient filter based solution
    - Efficient in memory solution (in progress, needs a fix)

## Trees

* Binary Search Tree with a really simple API:

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