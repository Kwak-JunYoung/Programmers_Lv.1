from itertools import combinations
def solution(numbers):
    answer = []
    comb_num = list(combinations(numbers, 2))
    
    for combi in comb_num:
        addition = sum(combi)
        if addition not in answer:
            answer.append(addition)
    
    answer.sort()
    return answer