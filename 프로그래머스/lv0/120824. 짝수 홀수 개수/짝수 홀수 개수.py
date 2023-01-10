def solution(num_list):
    a = []
    b = []
    for i in num_list:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    a = len(a)
    b = len(b)
    answer = [a,b]
    return answer