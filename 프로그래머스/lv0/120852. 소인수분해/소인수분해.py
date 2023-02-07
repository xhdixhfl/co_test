def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            k = n // i
            a = [k//l for l in range(2, k) if k % l == 0]
            if len(a)== 0 and k != 1:
                answer.append(k)
    answer.sort()
            
    return answer