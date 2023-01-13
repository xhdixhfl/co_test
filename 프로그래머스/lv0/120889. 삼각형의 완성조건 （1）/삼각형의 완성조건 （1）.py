def solution(sides):
    sides.sort()
    x = sides[2]
    a,b = sides[0],sides[1]
    if a+b > x:
        answer = 1
    else:
        answer = 2
    return answer