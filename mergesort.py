#mergesort function takes in [a] and returns sorted [a]
def mergesort(alist):
	print("sorting",alist)
	if(len(alist) > 1):
		mid = len(alist) / 2
		lefthalf = alist[:mid] 
		righhalf = alist[mid:]
		mergesort(lefthalf)
		mergesort(righhalf)

		i = 0
		j = 0
		k = 0

		while i < len(lefthalf) and j < len(righhalf):






#Setting up test case, should look into automated 
test = [2,500,1,-2,8,9,1,2,4,102]
a = mergesort(test)
assert(a == test.sort())
print("It's all good")