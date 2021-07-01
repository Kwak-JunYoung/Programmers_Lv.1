def solution(absolutes, signs):
    answer = 0
    length = len(absolutes)
    
    for i in range(length):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer