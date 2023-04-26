def solution(lines):
    answer = 0
    count = {}
    dots = [i+0.5 for i in range(lines[0][0], lines[0][-1])] +\
    [i+0.5 for i in range(lines[1][0], lines[1][-1])] + \
    [i+0.5 for i in range(lines[2][0], lines[2][-1])]
    # 중복되는 점수 사전화
    for d in dots:
        try: count[d] += 1   
        except: count[d] = 1 # 쌍추가
    # 2개 이상인 점 개수 세기 
    for d_v in count.values():
        if d_v != 1:
            answer +=1
        
    return answer