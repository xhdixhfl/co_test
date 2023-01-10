def solution(my_string, num1, num2):
    a = list(my_string)
    x = a[num1]
    y = a[num2]
    a[num1] = y
    a[num2] = x
    answer = ''.join(a)

    return answer