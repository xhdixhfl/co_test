def solution(chicken):
    service = 0
    ck = chicken
    
    while ck >= 10:
        eat = ck // 10
        service += eat
        ck = ck % 10 + eat
        
    return service
