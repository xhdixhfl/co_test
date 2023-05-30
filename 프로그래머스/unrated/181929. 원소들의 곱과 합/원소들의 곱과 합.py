from functools import reduce

def solution(num_list):
    a = reduce(lambda x, y: x * y, num_list)
    
    return 1 if a < sum(num_list)**2 else 0