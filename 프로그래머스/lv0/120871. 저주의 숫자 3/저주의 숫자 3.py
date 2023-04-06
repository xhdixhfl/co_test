def solution(n):
    # 출제되는 최대 3x마을의 수 리스트
    num_l = [i for i in range(1,230)]
    answer = []
    for num in num_l:
        if num % 3 != 0 and '3' not in str(num):
            answer.append(num)
            
    return answer[n-1]