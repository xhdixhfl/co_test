def solution(arr):
    answer = 0
    x = 0
    for i in arr:
        x += i
    answer = x / len(arr)
    return answer