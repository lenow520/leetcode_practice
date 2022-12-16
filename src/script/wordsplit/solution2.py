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

def find_headtail(sorted_word, fullname):
    for word in sorted_word:
        splited = fullname.split(word)
        head= None
        tail= None
        # print(splited)
        if len(splited)==2 and '' in splited:
            if splited[0]=='': 
                if binarysearch(splited[1], sorted_word):
                    head = word
                    tail = splited[1]
                    break

            else: 
                if binarysearch(splited[0] , sorted_word):
                    head = splited[0]   
                    tail = word
                    break

    return head, tail
    

def WordSplit(strArr): 
    target = strArr[0]

    dictionary = strArr[1]
    words = dictionary.split(",")
    sorted_word = sorted(words)
    
    head, tail = find_headtail(sorted_word, target)

    if head is None and tail == head:
        return('not possible')
    else:
        output = head+","+tail
        return output