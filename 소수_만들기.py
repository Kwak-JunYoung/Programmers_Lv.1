from itertools import combinations

def solution(nums):
    answer = 0
    print(type(nums))
    additions = [sum(i) for i in list(combinations(nums, 3))]
    for adds in additions:
        right = True
        for i in range(2, adds):
            if adds % i == 0:
                right = False
        if right:
            answer += 1
                
    return answer