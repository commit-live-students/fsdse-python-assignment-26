def solution(dic1, key1):
    '''Enter Code Here'''
    for i in dic1:
        if (i == key1):
            dic1.pop(key1)
            break

    return dic1

solution({1:10, 2:20, 3:30}, 2)
