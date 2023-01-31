def solution(num, total):
    answer = [(total//num ) - (num//2) if num % 2 == 1 else (total//num)-(num//2)+1]
    a = [i for i in range(answer[0], answer[0]+num)]
    return a