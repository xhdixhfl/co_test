def solution(s):
    ss = [int(i) for i in s.split(' ')]
    answer = [str(min(ss)), str(max(ss))]
    # answer.extend([str(min(ss)), str(max(ss))])
    return ' '.join(answer)