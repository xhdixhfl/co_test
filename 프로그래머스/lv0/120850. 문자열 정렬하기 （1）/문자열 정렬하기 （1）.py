def solution(my_string):
    answer = [int(i) for i in list(my_string) if i.islower() == False]
    answer.sort()
    return answer