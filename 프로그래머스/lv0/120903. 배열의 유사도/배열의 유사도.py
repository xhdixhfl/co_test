def solution(s1, s2):
    x = set(s1) 
    y = set(s2)
    
    return len(x & y)