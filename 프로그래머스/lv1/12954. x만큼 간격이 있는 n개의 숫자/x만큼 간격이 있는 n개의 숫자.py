def solution(x, n):
    return [x+(x*i) if i is not 0 else x for i in range(n) ]