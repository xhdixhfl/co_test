def solution(numbers, direction):
    answer = 0  # list에 두개이상 추가는 extand
    if direction == 'left':
        a = numbers[0]
        del numbers[0]
        numbers.append(a)
    elif direction == 'right':
        a = numbers[-1]
        del numbers[-1]
        numbers.insert(0,a)
    return numbers