def solution(s):
    p = 0
    y = 0
    for i in list(s):
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1
    answer = [True if p == y or (p==0 and y==0) else False]

    return answer[0]