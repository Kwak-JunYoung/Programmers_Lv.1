def solution(board, moves):
    answer = 0
    stacks = []
    basket = []
    size = len(board)
    for i in range(size):
        line = []
        for j in range(size):
            if board[j][i] != 0:
                line.append(board[j][i])
        stacks.append(line)
    
    for move in moves:
        pickup = stacks[move - 1]
        if len(pickup) == 0:
            continue
        if basket[-1:] == [pickup[0]]:
            basket.pop(-1)
            pickup.pop(0)
            answer += 2
        else:
            basket.append(pickup[0])
            pickup.pop(0)
    return answer