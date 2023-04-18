def solution(s):
    ss = s.split(' ')
    answer = []
    for i in ss:
        if i == "":
            answer.append('')
        elif i[0] in '1234567890':
            answer.append(i[0]+i[1:].lower())
        else:
            answer.append(i.capitalize())
    return ' '.join(answer)