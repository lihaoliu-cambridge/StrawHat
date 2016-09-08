L = [2, 3, -5, 20, 7]
max = L[0]
sum = 0
for i in L:
    sum += i
    if sum > 0:
        if sum >= max:
            max = sum
    else:
        sum = 0
print max