def solution(n):
    def div_n(n):
        divisorsList = []

        for i in range(1, int(n**(1/2)) + 1):
            if (n % i == 0):
                divisorsList.append(i) 
                if ( (i**2) != n) : 
                    divisorsList.append(n // i)

        divisorsList.sort()
    
        return divisorsList
    
    answer = []
    for i in range(1,n+1):
        a = div_n(i)
        if len(a) >= 3:
            answer.append(a)
                
    return len(answer)