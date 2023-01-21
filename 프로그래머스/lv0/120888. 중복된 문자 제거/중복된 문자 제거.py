def solution(my_string):
    text = []
    answer = [text.append(i) for i in list(my_string) if i not in text ]
    return ''.join(text)