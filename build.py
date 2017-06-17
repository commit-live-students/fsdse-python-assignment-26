def solution(dic1, key1):
    if key1 in dic1.keys():
        dic1.pop(key1,None)
    else:
        pass
    print dic1
    return dic1

solution({1:10,2:20},3)
