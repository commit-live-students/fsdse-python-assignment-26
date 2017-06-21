# Remove a key from a dictionary

dic = {1:10, 2:20, 3:30}

key = 5
def solution(d, k):
    if (d.has_key(k) == True):
        d.pop(k)
    else:
        return d
    return d

solution(dic, key)
#DOne, Not Posted =================================================================================
