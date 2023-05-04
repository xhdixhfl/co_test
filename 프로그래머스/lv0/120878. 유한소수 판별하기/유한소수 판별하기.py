def solution(a,b):
    answer = 1
    mcd = 0

    for i in range(min(a,b),0,-1):
        if a % i == b % i == 0:
            mcd = max(mcd,i)

    # 최대공약수로 나누면 기약분수됨
    a,b = a//mcd, b//mcd

    if a == b:
        answer = 1

    else:
        tmp = []
        for i in range(2,b+1):
            while b % i == 0:
                b //= i
                tmp.append(i)

        if all(x in (2,5) for x in tmp):
            answer = 1
        else:
            answer = 2

    return answer
