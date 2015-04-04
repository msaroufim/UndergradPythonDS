class MergeSort(object):

    def _merge(self,left, right):
    	"""
		Takes two sorted alistays left and right and merges them
		
		Not to be called externally

		Required arguments:
			left
			right
    	"""
        nl = len(left)
        nr = len(right)
        result = [0]*(nl+nr)
        i=0
        j=0
        for k in range(len(result)):
            if nl>i and nr>j:
                if left[i] <= right[j]:
                    result[k]=left[i]
                    i+=1
                else:
                    result[k]=right[j]
                    j+=1
            elif nl==i:
                result[k] = right[j]
                j+=1
            else: #nr>j:
                result[k] = left[i]
                i+=1
        return result

    def sort(self,alist):
    	"""
		sort step that recursively splits alistay into 
		two parts and then sorts them

		:type alist: list
		:param alist: List to sort
		:returns: list -- Sorted list
    	"""
        n = len(alist)
        if n<=1:
            return alist 
        left = self.sort(alist[:n/2])
        right = self.sort(alist[n/2:] )
        return self._merge(left, right)


#Test it out
def main():
    import random
    import time
    a = range(100000)
    random.shuffle(a)
    MergeSortInstance = MergeSort()

    t0 = time.time()
    result = MergeSortInstance.sort(a)
    t1 = time.time()
    total_time = t1 - t0
    #assert against the builtin sort method
    #result of builtin sorting algorithm

    #result of 
    print result
    print("Amount of time taken is",total_time)


if __name__ == '__main__':
    main()
