def solution(dic1, key1):
    '''Enter Code Here'''
    for k in dic1:
        if (k == key1):
            dic1.pop(key1)
            break
    print dic1
    return dic1

solution({1:10, 2:20, 3:30}, 2)
