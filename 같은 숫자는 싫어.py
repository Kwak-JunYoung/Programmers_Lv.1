def solution(arr):
    answer = []
    before = -1
    for i in arr:
        if i != before:
            answer.append(i)
        before = i
    return answer