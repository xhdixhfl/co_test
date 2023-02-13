def solution(my_string):
    s = my_string.split(' ')
    # answer = [int(s[0]) + int(s[-1]) if s[1] == '+' else int(s[0]) - int(s[-1])]
    p = [int(s[0]),]
    m = []
    for i, v in enumerate(s):
        if v == '+':
            p.append(int(s[i+1]))
            # answer += int(s[i-1]) + int(s[i+1])
        elif v == '-':
            m.append(int(s[i+1]))
            # answer += int(s[i-1]) - int(s[i+1])
    return sum(p) - sum(m)