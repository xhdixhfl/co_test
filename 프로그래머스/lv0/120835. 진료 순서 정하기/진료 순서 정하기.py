def solution(emergency):
    answer = []
    e = emergency[:]
    e.sort(reverse=True)
    def add_one(n):
        return n + 1
    return  list(map(add_one, list(map(e.index, emergency))))