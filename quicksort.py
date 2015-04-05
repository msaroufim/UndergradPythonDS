class QuickSort:


	def filterQuickSort(self,alist):
		"""
		Functional style implementation using filters
		Elegant but highly inneficient since filter needs
		to scan the whole list and evaluate the filter predicate on each element
		O(N!) is not gonna work in the real world no matter how elegant this is
		"""
		if alist == []:
			return alist
		pivots  = [x for x in alist if x == alist[0]]
		lesser  = self.filterQuickSort([x for x in alist if x < alist[0]])
		greater = self.filterQuickSort([x for x in alist if x > alist[0]])
		return lesser + pivots + greater


	def inPlaceImperativeQuickSort(self,alist):
		"""
		Imperative style in place implementation
		Use this!
		Optimal in space O(N)
		O(N log N) in average case
		""" 
		

		def _partition(alist,begin,end):
			#Can also pick random pivot
			#import random
			#pivot = random.choice(alist)
			pivot = begin
			for i in range(begin + 1 , end + 1):
				if alist[i] <= alist[begin]:
					pivot += 1
					alist[i],alist[pivot] = alist[pivot], alist[i]
			alist[pivot],alist[begin] = alist[begin],alist[pivot]
			return pivot
		
		def _quicksort(alist,begin = 0, end = None):
			if end is None:
				end = len(alist) - 1
			if begin >= end:
				return
			pivot = _partition(alist,begin,end)
			_quicksort(alist,begin,pivot - 1)
			_quicksort(alist,pivot + 1, end)

		_quicksort(alist)
		return alist



#Test it out
def main():
    import random
    import time
    a = range(20)
    random.shuffle(a)
    print a
    QuickSortInstance = QuickSort()

    t0 = time.time()
    result = QuickSortInstance.filterQuickSort(a)
    t1 = time.time()
    total_time = t1 - t0

    b = range(20)
    random.shuffle(b)
    t0 = time.time()
    result2 = QuickSortInstance.inPlaceImperativeQuickSort(b)
    t1 = time.time()
    total_time_2 = t1 - t0
    print result2
    print("Amount of time taken is",total_time)


if __name__ == '__main__':
    main()