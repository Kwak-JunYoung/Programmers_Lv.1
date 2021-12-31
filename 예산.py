def solution(d, budget):
    answer = 0
    d.sort(reverse = True)
    length = len(d)
    
    for i in range(length):
        if (sum(d[i:])) <= budget:
            return length - i
    
    return answer