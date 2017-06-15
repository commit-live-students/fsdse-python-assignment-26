def solution(dic1, key1):
    '''Enter Code Here'''
    dic1.pop(key1, None)
    return dic1


a = {1:10, 2:20, 3:30}
key = 2

print solution(a,key)
