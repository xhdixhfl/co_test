import itertools as it
def solution(dots):
    x = [a for a,b in dots]
    y = [b for a,b in dots]
    answer = 0

    if (y[0]-y[1])/(x[0]-x[1]) == (y[2]-y[3])/(x[2]-x[3]):
        answer += 1
    elif (y[0]-y[2])/(x[0]-x[2]) == (y[1]-y[3])/(x[1]-x[3]):
        answer += 1
    elif (y[0]-y[2])/(x[0]-x[2]) == (y[3]-y[1])/(x[3]-x[1]):
        answer += 1
    else:
        pass
    return answer
