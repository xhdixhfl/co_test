def solution(rny_string):
    answer = ['rn' if s == 'm' else s for s in rny_string]
    return ''.join(answer)