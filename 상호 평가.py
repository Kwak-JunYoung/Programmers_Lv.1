def solution(scores):
    s_list = ['F', 'F', 'F', 'F', 'F', 'D', 'D', 'C', 'B', 'A', 'A']
    answer = ''
    length = len(scores)
    for i in range(length):
        for j in range(i, len(scores[0])):
            scores[i][j], scores[j][i] = scores[j][i], scores[i][j]
    for i in range(length):
        average = 0
        if (max(scores[i]) == scores[i][i] and scores[i].count(max(scores[i])) == 1):
            average = (sum(scores[i]) - max(scores[i])) / (len(scores[i]) - 1)
        elif (min(scores[i]) == scores[i][i] and scores[i].count(min(scores[i])) == 1):
            average = (sum(scores[i]) - min(scores[i])) / (len(scores[i]) - 1)
        else:
            average = sum(scores[i]) / len(scores[i])

        answer += s_list[int(average // 10)]
    return answer