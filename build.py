def solution(dic1, key1):
    if key1 in dic1.keys():
        del dic1[key1]
    return dic1


dic1 = {1:10, 2:20, 3:30}
key1 = 2
