def solution(dartResult):
    score_board = []
    i = 0
    char_list = ['S', 'D', 'T']
    length = len(dartResult)
    
    while i < length:
        if str(dartResult[i]).isnumeric():
            if str(dartResult[i + 1]).isalpha():
                score_board.append(int(dartResult[i]) ** (char_list.index(dartResult[i + 1]) + 1))
                i += 2
            elif str(dartResult[i + 1]).isnumeric():
                score_board.append(int(dartResult[i: i + 2]) ** (char_list.index(dartResult[i + 2]) + 1))
                i += 3

        elif dartResult[i] == '*':
            score_board[-1] *= 2
            if len(score_board) > 1:
                score_board[-2] *= 2
            i += 1
        
        elif dartResult[i] == '#':
            score_board[-1] *= (-1)
            i += 1
            
    return sum(score_board)