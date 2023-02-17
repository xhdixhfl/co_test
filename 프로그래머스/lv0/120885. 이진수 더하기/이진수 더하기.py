def solution(bin1, bin2):
    answer = list(bin(int(bin1,2) + int(bin2, 2)))
    del answer[:2]
    return ''.join(answer)