def solution(cipher, code):
    answer = [x for i, x in enumerate(list(cipher))\
    if code <= (i+1) and (i+1) % code == 0]

    return ''.join(answer)