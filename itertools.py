import itertools

lst = range(4)
result = list(itertools.comb(lst, 2))  # output of print statement is now shown

print(result) # prints: [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

#From http://pymotw.com/2/itertools

