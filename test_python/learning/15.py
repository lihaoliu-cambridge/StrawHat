double_flag = False
for i in range(len(L)):
    if i == 0:
        if L[i] in L[1:]:
            break
    elif i == len(L)-1:
        if L[i] in L[:-1]:
            break
    else:
        if L[i] in L[0:i]+L[i+1:]:
            break
else:
    double_flag = True
if double_flag:
    print 'NO'
else:
    print 'YES'