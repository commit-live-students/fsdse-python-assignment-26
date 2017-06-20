def solution(dic1, key1):
    my_dict = dic1
    my_key = key1
    if my_key in my_dict.keys() :
        my_dict.pop(my_key)
    return my_dict

dict_available = {1:10, 2:20, 3:30}
solution(dict_available,4)
