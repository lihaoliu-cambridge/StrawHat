from collections import defaultdict

C = defaultdict(str)

C[(0,0)]='ASSDSD'
print C[(0,0)]
print C[1]

print C

s = "the quick brown fox jumps over the lazy dog"

words = s.split()
location = defaultdict(list)
for m, n in enumerate(words):
    location[n].append(m)

print location
