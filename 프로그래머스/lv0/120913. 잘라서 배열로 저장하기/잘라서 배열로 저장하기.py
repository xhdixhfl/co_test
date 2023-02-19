def solution(my_str, n):
    if len(my_str)%n==0:
        answer = [f'{my_str[(i-1)*n : i*n]}' for i in range(1, (len(my_str)//n) +1)]
    else:
        answer = [f'{my_str[(i-1)*n : i*n]}' for i in range(1,(len(my_str)//n) +1)]
        answer.append(f'{my_str[-(len(my_str)%n):]}')
    return answer