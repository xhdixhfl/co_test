def solution(board):
    # 지뢰에 영향받는 칸들
    row = [-1,0,1]
    col = [-1,0,1]
    answer = 0 # 안전지대
    danger_zone = [[0] * len(board) for _ in range(len(board))]
    danger_index = []
    for r in row:
        for c in col:
            danger_index.append((r,c))
 # 적용
    for ir, row in enumerate(board):
        for ic, col in enumerate(row):
            if board[ir][ic] == 1:
                for r,c in danger_index:
                    try: # 지뢰에 영향을 받는 위치
                        if ir+r<0 or ic+c<0 or ir+r>len(board) or ic+c>len(board):
                            continue
                        danger_zone[ir+r][ic+c] = "X"
                        danger_count += 1
                    except:
                        continue
    for ir, row in enumerate(danger_zone):
        for ic, col in enumerate(row):
            if danger_zone[ir][ic] == 0:
                answer += 1
            
    return answer