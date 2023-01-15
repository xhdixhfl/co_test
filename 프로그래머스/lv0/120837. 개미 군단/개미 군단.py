def solution(hp):
    answer = 0
    if hp % 5 == 0:
        answer = hp//5
    elif 0 < hp % 5 < 3:
        answer = (hp//5) + (hp%5)
    else:
        answer = (hp//5) + (hp%5) % 3 + 1
    return answer