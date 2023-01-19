def solution(num, k):
    if str(k) in list(str(num)):
        a = list(str(num)).index(str(k)) + 1
    else:
        a = "-1"
    return int(a)