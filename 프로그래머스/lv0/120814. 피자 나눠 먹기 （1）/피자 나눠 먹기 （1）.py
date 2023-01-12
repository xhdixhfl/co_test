def solution(n):
    if n%7 == 0:
        answer = n//7 + 0
    else:
        answer = n//7 + 1
    return answer


def solution(n):
    # 리스트내포의 if-else문 [참인경우 참의 조건 거짓 조건]
    answer = [n//7 + 0 if n%7 == 0 else n//7 + 1][0]

    return answer
