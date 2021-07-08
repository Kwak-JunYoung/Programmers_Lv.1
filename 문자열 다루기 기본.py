def solution(s):
    answer = True
    length = len(s)
    answer = (length == 4) or (length == 6)    
    for i in range(length):
        if s[i] not in "0123456789":
            answer = False
    return answer