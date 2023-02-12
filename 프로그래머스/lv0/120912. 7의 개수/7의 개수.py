def solution(array):
    answer = [list(str(i)).count("7") for i in array]
    return sum(answer)