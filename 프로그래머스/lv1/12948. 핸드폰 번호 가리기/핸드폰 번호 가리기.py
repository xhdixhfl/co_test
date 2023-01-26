
def solution(phone_number):
    a = list(str(phone_number))
    b = ''.join(a[-4:])
    c = '*' * (len(a) - 4)
    return c+b