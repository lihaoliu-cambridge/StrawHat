"""
note:
1.heapify: this process is begin from total_size//2 to 1,
 and for each point it have to iter down to the bottom to make sure it remain balance.

2.heappush: this process is begin add the new node to the last and then iter it to the proper position.

3.heappop: switch the first and last node, and begin resort(like heapify) from the begin node to the second last one)
"""
from heapq import heapify, heappush, heappop
from itertools import count


# this is a classic greedy algorithm
def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa + fb, n, [a, b]))
        print trees
    return trees


seq_1 = 'abcdefghi'
frq_1 = [4, 5, 6, 9, 11, 12, 15, 16, 20]

huffman(seq_1, frq_1)
