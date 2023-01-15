def solution(n):
    a = int(n ** (1/2))
    if a**2 == n:
        answer = 1
    else:
        answer = 2
    
    return answer