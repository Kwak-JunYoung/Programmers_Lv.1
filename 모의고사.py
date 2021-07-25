def solution(answers):
    answer = []
    ans_cand = []
    one = 0
    two = 0
    three = 0
    tw_ad = [1, 3, 4, 5]
    th_ad = [3, 1, 2, 4, 5]
    length = len(answers)
    for i in range(length):
        
        if (i % 5 + 1) == answers[i]:
            one += 1
            
        if th_ad[(i//2)%5] == answers[i]:
            three += 1
            
        cond_a = ((i % 2 == 0) and (answers[i] == 2))
        cond_b = ((i % 2 == 1) and (answers[i] == tw_ad[(i // 2) % 4]))
        if cond_a or cond_b:
            two += 1
    
    ans_cand.append(one)
    ans_cand.append(two)
    ans_cand.append(three)
    maxans = max(one, two, three)
    for i in range(3):
        if ans_cand[i] == maxans:
            answer.append(i + 1)
            
    return answer