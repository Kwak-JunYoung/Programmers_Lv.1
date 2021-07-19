def solution(s):
    answer = ''
    word_list = s.split(' ')
    for word in word_list:
        for i in range(len(word)):
            if (i % 2 == 0):
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += " "
    
    return answer[:-1]