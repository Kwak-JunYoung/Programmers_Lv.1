def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    if len(answer) == 0: answer.append(-1)
    return sorted(answer)