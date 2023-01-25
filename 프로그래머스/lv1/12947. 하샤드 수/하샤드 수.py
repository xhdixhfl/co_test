def solution(x):
    a = []
    for i in list(str(x)):
        a.append(int(i))
    if x % sum(a) == 0:
        answer = True
    else:
        answer = False
    return answer