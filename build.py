def solution(d1, key):
    '''Enter Code Here'''
    lst = []
    new_dic = {}
    for i in d1.items():
        if i[0] != key:
            lst.append(i)
    new_dic.update(lst)
    return new_dic

d1 = {1:10, 2:20, 3:30}
k1 = 2

d2 = {1:10, 2:20, 3:30}
k2 = 4

print(solution(d1, k1))
print(solution(d2, k2))
