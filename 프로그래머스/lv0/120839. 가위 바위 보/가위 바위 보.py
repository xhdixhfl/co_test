def solution(rsp):
    a = []
    for i in list(rsp):
        if i == '2':
            a.append('0')
        elif i == '5':
            a.append('2')
        else:
            a.append('5')
            
    return ''.join(a)