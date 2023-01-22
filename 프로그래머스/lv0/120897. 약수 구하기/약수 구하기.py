def solution(n):
    answer = [i for i in range(1, n+1) for j in range(1, n+1) if i*j == n]
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         if i * j == n:
    #             if i not in answer:
    #                 answer.extend((i,j))
    answer.sort()
    
    
    return answer