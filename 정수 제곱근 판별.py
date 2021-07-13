import math
def solution(n):
    answer = 0
    rooted = math.sqrt(n)
    if rooted.is_integer():
        answer = (rooted+1) ** 2
    else:
        answer = -1
    return answer