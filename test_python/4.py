from pandas import Series, DataFrame

a = {'a': 1, 'b': 2, 'c': 3}
b = ['a', 'b', 'c', 'd']

s = Series(a, index=b)
print s['d']

e = {1: {2: 'z', 3: 'y'}, 4: {5: 'A', 6: 'B'}}
f = DataFrame(e)
print f.values()[0]
