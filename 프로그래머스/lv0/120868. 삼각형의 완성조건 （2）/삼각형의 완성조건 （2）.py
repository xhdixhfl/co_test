def solution(sides):
    # sides에 가장 긴 변이 있는 경우
    one = [i for i in range(max(sides)-min(sides),max(sides)) if (i + min(sides)) > max(sides)]
    answer = [i for i in range(max(sides), sum(sides))]
    return len(answer)+len(one)