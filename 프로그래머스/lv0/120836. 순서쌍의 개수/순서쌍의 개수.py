import math
def solution(n):
    a = [i for i in range(1, n+1) if n%i ==0]
    # for i in range(1,n+1):
    #     if n % i == 0:
    #         a.append(i)
    # # answer = 0
    return len(a)
