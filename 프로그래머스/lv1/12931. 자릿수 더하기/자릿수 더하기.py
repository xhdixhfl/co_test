
def solution(n):
    answer = 0
    x = len(str(n))
    a = list(str(n))
    print(a)
    for i in range(x):
        answer += int(a[i])
    return answer