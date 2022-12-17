def LDS(seq):
    n = len(seq)
    arr = sorted(seq)
    divsubset = [[ele] for ele in arr]
    
    max_value = 1
    for i in range(n):
        main_div = arr[i]
        maxsize = 1
        candidate=[]
        for j in range(i):
            if main_div%(divsubset[j][-1])==0 and maxsize<=len(divsubset[j]):
                maxsize = len(divsubset[j])
                candidate = divsubset[j]
        divsubset[i] = candidate+divsubset[i]
        if max_value < len(divsubset[i]):
            max_value = len(divsubset[i])
    
    #print(divsubset)
                
    return max_value

inputarr = [1, 2, 4, 5, 8, 10]
ans = LDS(inputarr)
print(ans)

inputarr = [1, 16, 7, 8, 4]
ans = LDS(inputarr)
print(ans)

inputarr = [1,2,3]
ans = LDS(inputarr)
print(ans)

inputarr = [1,2,4,8]
ans = LDS(inputarr)
print(ans)

inputarr = [1,2,7,8,45,56,28]
ans = LDS(inputarr)
print(ans)