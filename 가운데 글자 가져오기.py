def solution(s):
    answer = ''
    length = len(s)
    
    if length % 2:
        answer = answer = s[int(length / 2)]
        
    else:
        answer = s[int(length / 2)-1] + s[int(length / 2)]
    return answer