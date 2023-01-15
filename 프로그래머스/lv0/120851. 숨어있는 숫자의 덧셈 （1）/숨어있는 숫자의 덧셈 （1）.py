def solution(my_string):
    a = ['1','2','3','4','5','6','7','8','9','0']
    answer = 0
    for i in range(10):
        if a[i] in list(my_string):
            x = list(my_string).count(a[i])
            answer += int(a[i]) * x

    return answer