def solution(myString):
    return ''.join([t.upper() if t == 'a' or t == 'A' else t.lower() for t in myString])