def solution(n):
    answer = 0
    rev_tri = ''
    while n:
        rev_tri += str(n % 3)
        n //= 3
        
    length = len(rev_tri)
    for i in range(length):
        answer += (int(rev_tri[length - i - 1]) * (3 ** i))
    return answer