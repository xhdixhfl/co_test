
def solution(my_string):
    a =[ i.lower() for i in list(my_string)]
    a.sort()
    return ''.join(a)