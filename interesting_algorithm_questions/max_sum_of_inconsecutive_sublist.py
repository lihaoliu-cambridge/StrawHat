# time complexity is o(nlogn)
# better use tmp_max to record replace the second max
for i in range(2, len(L)):
    before_max = max(0, max(L[0: i-1]))
    L[i] = L[i] + before_max
print max(L)