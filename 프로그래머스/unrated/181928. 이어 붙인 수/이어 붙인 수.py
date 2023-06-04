def solution(num_list):
    odd = []
    even = []
    for n in num_list:
        if n % 2 == 0:
            even.append(str(n))
        else:
            odd.append(str(n))
            
    return int(''.join(odd))+int(''.join(even))