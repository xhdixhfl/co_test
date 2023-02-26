def solution(numlist, n):
    # for idx, val in enumerate(numlist):
    #     if abs(val-n)
    answer = [[val, abs(val-n)] for val in numlist]
    numlist.sort(key = lambda x: (abs(n-x), -x))
    return numlist