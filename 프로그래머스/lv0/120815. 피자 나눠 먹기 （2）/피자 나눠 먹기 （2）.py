import math
def solution(n):
    answer = [i for i in range(1, n+1)  if (6*i)%n ==0]
    # if n % 6 == 0:
    #     answer = [n // 6]
    # else:
    #     for i in range(1,n+1):
    #         if (6*i) % n  == 0:
    #             answer.append(i)
    return answer[0]