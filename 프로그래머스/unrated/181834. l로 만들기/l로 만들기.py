def solution(myString):
    answer = ["a","b","c","d","e","f","g","h","i","j","k"]
    return ''.join(['l' if m in answer else m for m in myString])