def solution(quiz):
    dap = []
    for i in quiz:
        s = i.split(' ')
        if s[1] =='-':
            if int(s[-1]) == int(s[0]) - int(s[2]):
                dap.append('O')
            else:
                dap.append('X')
        else:
            if int(s[-1]) == int(s[0]) + int(s[2]):
                dap.append('O')
            else:
                dap.append('X')
            
    return dap