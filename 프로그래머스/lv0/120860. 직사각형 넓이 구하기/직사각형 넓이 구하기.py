def solution(dots):
    a = [dots[i][0] for i in range(len(dots))]
    b = [dots[i][1] for i in range(len(dots))]
#     abs((dots[1][0] - dots[3][0]) * abs((dots[2][1] - dots[1][1])))
    return (max(a)-min(a)) * (max(b)-min(b))