def solution(s1, s2):
    x = set(s1) 
    y = set(s2)
# 이런시도도 했었음.
    # a1= [x for i in s2 for x in s1 if x in i]
    # a2= [x for i in s1 for x in s2 if x in i]
    # answer = [x for i in a2 for x in a1 if x in i]    
    return len(x & y)
