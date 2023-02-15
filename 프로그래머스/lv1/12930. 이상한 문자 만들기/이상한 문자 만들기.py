def solution(s):
    answer = s.split(' ')
    b = []
    for a in answer:
        dap = [a[i].upper() if i ==0 or i % 2==0 else a[i].lower() for i in range(len(a))]
        b.append(dap)

            
    return ' '.join([''.join(b[i]) for i in range(len(b))])