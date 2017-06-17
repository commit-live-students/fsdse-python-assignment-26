def solution(dic1, key1):
    d={}
    if key1 not in dic1:
        return dic1
    else:
        del dic1[key1]
        d=dic1
        return d
