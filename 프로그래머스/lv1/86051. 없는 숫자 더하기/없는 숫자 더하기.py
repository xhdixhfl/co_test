def solution(numbers):
    answer = [i for i in list(range(10)) if i not in numbers]
    return sum(answer)