def solution(dic1, key1):
    '''Enter Code Here'''

    for i in dic1:
        if i == key1:
            del dic1[key1]
            return dic1

    return dic1



'''
dic1 = {1: 10, 2: 20, 3: 30}
a = solution(dic1,4)
print a
'''
