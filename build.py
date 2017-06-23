def solution(dic1, key1):
    print(dic1)
    if key1 in dic1:
        del dic1[key1]
    return dic1
print solution(({'a':1,'b':2,'c':3,'d':4}),'a')
