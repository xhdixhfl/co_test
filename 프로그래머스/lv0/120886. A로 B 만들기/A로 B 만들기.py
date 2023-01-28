def solution(before, after):
    b = list(before)
    a = list(after)
    for i in b:
        if i in a:
            del a[a.index(i)]
    if len(a)>= 1:
        answer = 0
    else:
        answer = 1
    return answer