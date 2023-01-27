def solution(s):
    answer = [list(s)[(len(list(s)) // 2) - 1 : (len(list(s)) // 2) +1 ] \
              if len(list(s))%2==0 else list(s)[len(list(s)) // 2]]
    return ''.join(answer[0][0:2])