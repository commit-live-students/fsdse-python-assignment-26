def solution(dic1, key1):
    popped_key = dic1.pop(key1,None)

    if popped_key != None:
        #print "popped ",dic1
        return dic1
    #print "un-popped",dic1
    return dic1

dic1 = {1:10, 2:20, 3:30}
key1 = 4
solution(dic1, key1)
