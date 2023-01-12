def solution(dot):
    x,y = dot
    if x>0 and y>0:
        answer = 1
    elif x>0 and y<0:
        answer = 4
    elif x<0 and y<0:
        answer = 3
    else:
        answer =2
    return answer