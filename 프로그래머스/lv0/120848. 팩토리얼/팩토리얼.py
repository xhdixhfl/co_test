def solution(n):
    answer = 1
    a =[]
    #while answer < n:
    for i in range(1, n+1):
        answer *= i 
        if answer > n:
            break
        else:
            a.append(i)
    return a[-1]