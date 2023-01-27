def solution(absolutes, signs):
    answer = [absolutes[i] if v == True \
              else (-1*absolutes[i]) for i, v in enumerate(signs)]
    return sum(answer)