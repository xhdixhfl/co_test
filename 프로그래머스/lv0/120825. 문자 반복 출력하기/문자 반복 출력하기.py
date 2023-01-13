def solution(my_string, n):
    answer = []
    for idx, txt in enumerate(my_string):
        answer.append(txt * n)
        
    return ''.join(answer)

