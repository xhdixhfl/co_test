def solution(my_string):
    down = ['a','b','c','d','e','f','g','h','i','j','k','l','m',\
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer = []
    for i in list(my_string):
        if i in down:
            answer.append(i.upper())
        elif i not in down:
            answer.append(i.lower())
    return ''.join(answer)