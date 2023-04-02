def solution(spell, dic):
    ex =  set(spell)
    answer = 0
    for d in dic:
        if set(d) == ex:
            answer += 1
        else:
            pass
            
    return [1 if answer >= 1 else 2][0]