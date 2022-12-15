def WordSplit(strArr): 
    target = strArr[0]

    dictionary = strArr[1]
    words = dictionary.split(",")

    first = []
    second = []
    for word in words:
        splited = target.split(word)
        
        if len(splited)==2 and '' in splited:
            # print(splited)
            if splited[0]=='': 
                first.append(word)
            else: 
                second.append(word)

    def combine_n_compare(first, second, target):
        for first_str in first:
            for second_str in second:
                fused = first_str+second_str
                # print(fused)
                if fused == target:

                    return first_str, second_str
        
        else: return None, None

    fir_str, sec_str = combine_n_compare(first, second, target)
    if fir_str is None and sec_str == fir_str:
        return('not possible')
    else:
        output = fir_str+","+sec_str
        return output