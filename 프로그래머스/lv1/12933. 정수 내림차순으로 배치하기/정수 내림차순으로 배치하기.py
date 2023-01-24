def solution(n):
    answer = [i for i in list(str(n))]
    answer.sort(reverse = True)
    return int(''.join(answer))