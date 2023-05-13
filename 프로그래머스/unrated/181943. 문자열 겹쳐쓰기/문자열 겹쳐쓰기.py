def solution(my_string, overwrite_string, s):
    ls = list(my_string)
    del ls[s:s+len(overwrite_string)]
    ls.insert(s,overwrite_string)            
    return ''.join(ls)