def solution(age):
    page = ['a','b','c','d','e','f','g','h','i','j']
    answer = [page[int(x)] for x in list(str(age)) ]
    return ''.join(answer)