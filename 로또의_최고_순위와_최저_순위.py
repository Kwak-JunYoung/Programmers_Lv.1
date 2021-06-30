def solution(lottos, win_nums):
    answer = []
    q_zero = 0
    count = 0

    for i in range(6):
        if lottos[i] == 0:
            q_zero += 1
            
        for j in range(6):
            if lottos[i] == win_nums[j]:
                count += 1

    min_possibility = count
    max_possibility = count + q_zero

    if min_possibility == 0:
        min_possibility = 1   

    if max_possibility == 0:
        max_possibility = 1

    answer.extend([7 - max_possibility, 7 - min_possibility])

    return answer