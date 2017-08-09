def solution(dic1, key1):
    dic1.pop(key1, None)
    return dic1

dic1 = {1:10, 2:20, 3:30}
print solution(dic1, 2)
