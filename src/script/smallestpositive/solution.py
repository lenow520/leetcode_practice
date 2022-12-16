def binarysearch(target, lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        middle = int((start + end)/ 2)
        midpoint = lst[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return True
    return False

def Solution(A):
    sorted_arr = sorted(A)
    max_value = sorted_arr[-1]
    if max_value<=0:
        return 1

    for i in range(1, max_value):
        if not binarysearch(i, sorted_arr):
            return i

    return max_value+1