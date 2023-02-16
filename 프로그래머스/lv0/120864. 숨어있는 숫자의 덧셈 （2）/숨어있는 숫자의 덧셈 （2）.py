import re
def solution(my_string):
    answer = [int(i) for i in re.findall(r'\d+', my_string)]

    return sum(answer)