def MaxAligned(arr, divisor):
    ans_dict = {}
    def add_key_value(dictionary,key):
        if key in dictionary:
            value = dictionary[key]
            dictionary[key] = value+1
        else:
            dictionary[key] = 1

    for ele in arr:
        # if ele>0:
        #     rmd = ele%divisor
        # else:
        #     rmd = ele%divisor + divisor
        rmd = ele%divisor
        # print(ele,"-->",rmd)
        add_key_value(ans_dict, rmd)
        
    ans = max(list(ans_dict.values()))
    return ans