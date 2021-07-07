def solution(s):
    answer = ''
    length = len(s)
    s_list = []
    for i in range(length):
        s_list.append(s[i])
    s_list.sort()
    for j in range(length):
        answer += s_list.pop()
    return answer