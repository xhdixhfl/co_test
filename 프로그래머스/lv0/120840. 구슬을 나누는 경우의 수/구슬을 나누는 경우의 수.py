from math import prod
def solution(balls, share):
    answer = 0
    b = [ i for i in range(1, balls + 1)]
    x = [ i for i in range(1, (balls-share)+1)]
    y = [ i for i in range(1, share+1)]
    answer = prod(b)/(prod(x)*prod(y))
    
    return answer