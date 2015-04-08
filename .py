#powerset python

#bunch of good very different answers
http://stackoverflow.com/questions/1482308/whats-a-good-way-to-combinate-through-a-set
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def powerset(seq):
"""
Returns all the subsets of this set. This is a generator.
"""
if len(seq) <= 1:
    yield seq
    yield []
else:
    for item in powerset(seq[1:]):
        yield [seq[0]]+item
        yield item

#lambda might impress scala kids
def powerset(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],lst, [[]])

#powerset
>>> def powerset(s):
...     x = len(s)
...     for i in range(1 << x):
...             print [s[j] for j in range(x) if (i & (1 << j))]

#List slicing
http://stackoverflow.com/questions/4486382/slice-operator-understanding
>>> a = [1,2,3,4]
>>> a[0:2] # take items 0-2, upper bound noninclusive
[1, 2]
>>> a[0:-1] #take all but the last
[1, 2, 3]
>>> a[1:4]
[2, 3, 4]
>>> a[::-1] # reverse the list
[4, 3, 2, 1]
>>> a[::2] # skip 2
[1, 3]


Notes on difference between spark and storm
http://stackoverflow.com/questions/24119897/apache-spark-vs-apache-storm

what is openmpi
http://www.open-mpi.org/