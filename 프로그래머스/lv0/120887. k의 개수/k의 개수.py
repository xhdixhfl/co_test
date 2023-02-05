def solution(i, j, k):
    answer = [x for l in range(i, j+1) for x in list(str(l))]
    return answer.count(str(k))