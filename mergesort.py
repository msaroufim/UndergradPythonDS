class MergeSort(object):
    def merge(self,left, right):
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

    def sort(self,arr):
        n = len(arr)
        if n<=1:
            return arr 
        left = self.sort(arr[:n/2])
        right = self.sort(arr[n/2:] )
        return self.merge(left, right)


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
