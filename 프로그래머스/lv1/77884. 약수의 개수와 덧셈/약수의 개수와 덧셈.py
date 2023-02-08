def solution(left, right):
    def pn(n):
        # pn = [x for x in range(1,n+1) for y in range(1, n+1) if x*y == n]
        pn = [x for x in range(1, n+1) if n % x == 0 ]
        if len(pn)%2 == 1:
            return -1 * n
        else:
            return n
    # answer = [pn(i) for i in range(left, right+1)]
    return sum([pn(i) for i in range(left, right+1)])