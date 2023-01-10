def solution(n, k):
    answer = 0
    a = n//10 # 음료수 무료 개수
    answer = 12000*n + 2000*(k-a)
    return answer