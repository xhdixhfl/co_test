def solution(price, money, count):
    wallet = [price * i for i in range(1, count+1)]
    answer = [abs(money-sum(wallet)) if money-sum(wallet) < 0 else 0]
    return answer[0]