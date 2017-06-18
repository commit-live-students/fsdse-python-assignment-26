dic1={1:10, 2:20, 3:30}
key1=2
def solution(dic1, key1):
    if dic1.has_key(key1):
        del dic1[key1]
        return dic1
    else:
        return dic1
solution (dic1,key1)
