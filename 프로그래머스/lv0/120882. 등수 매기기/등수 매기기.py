def solution(score):
    a = [sum(i)/2 for i in score]
    b = sorted(a, reverse = True)
    answer = [b.index(i)+1 for i in a]
    return answer