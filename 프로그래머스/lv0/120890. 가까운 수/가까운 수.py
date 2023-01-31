import numpy as np
def solution(array, n):
    answer = [abs(n - i) for i in array]
    npanswer = np.array(answer)
    a = []
    if len(np.where(npanswer == min(answer))[0]) > 1:
        for i in np.where(npanswer == min(answer))[0]:
            a.append(array[i])
        answer = min(a)
    else:
        answer = array[answer.index(min(answer))]

    return answer
