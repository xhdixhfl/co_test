def solution(order): 
    answer = [
    1 for i in range(len(str(order))) if str(order)[i] == '3' or str(order)[i] == '6' or str(order)[i] == '9'
    ]
    return sum(answer)