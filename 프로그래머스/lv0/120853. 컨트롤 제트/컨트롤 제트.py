def solution(s):
    answer = ''
    ss = s.split(' ')
    if "Z" in ss:
        a = [int(ss[i-1]) for i, v in enumerate(ss) if v=="Z"]
        fs = [int(i) for i in ss if i not in ["Z"]]
        answer = (sum(fs) - sum(a))
    else:
        answer = sum([int(i) for i in ss])
    return answer