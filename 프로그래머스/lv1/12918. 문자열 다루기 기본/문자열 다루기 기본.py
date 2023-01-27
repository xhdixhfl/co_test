import re
def solution(s):
    a= re.compile('[a-zA-Z]')
    return (len(s)==4 and a.search(s)==None) or (len(s)==6 and a.search(s)==None)