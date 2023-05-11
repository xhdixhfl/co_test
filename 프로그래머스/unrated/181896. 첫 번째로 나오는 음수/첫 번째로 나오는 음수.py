def solution(num_list):
    minus = []
    for i in range(len(num_list)):
        if num_list[i] < 0:
            minus.append(i)
        else:
            pass
    return minus[0] if len(minus)>0 else -1