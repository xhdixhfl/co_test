def solution(my_string, alp):
    answer = [i.upper() if i == alp else i for i in my_string]
    return ''.join(answer)