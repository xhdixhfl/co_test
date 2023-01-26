def solution(num):
    answer = ''
    for i in range(1,501):
        if num % 2 == 0:
            num = num / 2
            if num == 1:
                answer = i
                break
            elif i == 500 and answer != 1:
                answer = -1
        elif num % 2 == 1 and num != 1:
            num = (3 * num) + 1
            if num == 1:
                answer = i
                break
            elif i == 500 and answer != 1:
                answer = -1
        elif num == 1:
            answer = 0
    return answer