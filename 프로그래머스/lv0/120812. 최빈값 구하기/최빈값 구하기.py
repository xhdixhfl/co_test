def solution(array):
    answer = 0
    dic = {}
    for i in array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    answer = [key for key, value in dic.items() if value == max(dic.values())]
    if len(answer) > 1:
        answer = -1
    else:
        answer = answer[0]
            
    return answer