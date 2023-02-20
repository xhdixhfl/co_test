def solution(keyinput, board):
    limit_x = (board[0] - 1) // 2
    limit_y = (board[1] - 1) // 2

    commands = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0],
    }

    x = y = 0
    for command in keyinput:
        dx, dy = commands[command]
        nx, ny = x + dx, y + dy
        if abs(nx) <= limit_x and abs(ny) <= limit_y:
            x, y = nx, ny

    return [x, y]
    return one, two

# 이렇게 도전중 근데 8번이 계속 탈락됨
    # one = []
    # two = []
    # answer = [one.append(1) if i == 'right' else one.append(-1) if i == 'left' else two.append(1) if i == 'up' else two.append(-1) for i in keyinput]
    # if board[0]//2 >= abs(sum(one)):
    #     one = sum(one)
    # else:
    #     if sum(one)>0:
    #         one = board[0]//2
    #     else:
    #         one = -(board[0]//2)
    # if board[1]//2 >= abs(sum(two)):
    #     two = sum(two)
    # else:
    #     if sum(two)>0:
    #         two = board[1]//2
    #     else:
    #         two = -(board[1]//2)
