def solution(babbling):
    answer =['aya','ye','woo','ma']
    rep=[]
    for i in babbling:
        for j in answer:
            i=i.replace(j,'*') # i와 j가 같으면 *
            # print(i)
        rep.append(i)
    print(rep)
    cnt=0
    for i in rep:
        i=set(i) # *를 하나만 남기는 작업
        if len(i)==1 and '*' in i:  # *이 하나만 남는 경우가 가능한 발음과 같으니깐.
            cnt+=1
    return cnt