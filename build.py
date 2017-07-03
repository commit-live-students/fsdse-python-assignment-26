def solution(dic1, key1):
    for i in dic1:
        if (i == key1):
            dic1.pop(key1)
            break

    return dic1
