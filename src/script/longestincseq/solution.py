def LIS(seq):
    n = len(seq)
    if n == 0:
        return 0
    
    LISlen = [1]*n
    max_value = 1
    for i in range(n):
        headmax = 1
        for j in range(i):
            if seq[i]>seq[j] and headmax <= LISlen[j]:
                headmax = LISlen[j]+1
        LISlen[i] = headmax
        if LISlen[i]>max_value:

            max_value = LISlen[i]
            #print(max_value)
    print(LISlen)
    return max_value


inputseq =  [10,9,2,5,3,7,101,18]
ans = LIS(inputseq)
print(ans)
            
inputseq =   [1,4,2,4,2,3]
ans = LIS(inputseq)
print(ans)

inputseq =   [1,1,1,2]
ans = LIS(inputseq)
print(ans)