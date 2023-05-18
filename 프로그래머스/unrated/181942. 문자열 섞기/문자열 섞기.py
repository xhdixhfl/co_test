def solution(str1, str2):
    a = []
    for i in range(len(str1)):
        a.extend([str1[i],str2[i]])
    return ''.join(a)