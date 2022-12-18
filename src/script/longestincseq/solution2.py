def binarysearch(target, lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        middle = int((start + end)/ 2)
        midpoint = lst[middle]
        if midpoint < target:
            start = middle + 1
        else:
            end = middle - 1
    return start


def LIS(seq):
    n = len(seq)
    if n == 0:
        return 0
    
    magic = [seq[0]]
    for i in range(1, n):
        if magic[-1] < seq[i]:
            magic.append(seq[i])
        #elif magic[0] > seq[i]:
        #    magic[0] = seq[i]
        else:
            target = seq[i]
            index = binarysearch(target, magic)
            print(target,index)
            magic[index] = target
            #left = magic[:index]
            #magic = left+[target]
    print(magic)
    max_value = len(magic)       
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

inputseq =   [2,1,2,4,5,3,8,2,4,-3]
ans = LIS(inputseq)
print(ans)