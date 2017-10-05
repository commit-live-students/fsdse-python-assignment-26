def solution(dict, key):
    '''Enter Code Here'''
    if key in dict:
        del dict[key]
    return dict
