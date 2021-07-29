def solution(N, stages):
    reached = []
    fail_rate = []
    cur = len(stages) 
    for i in range(1, N+1):
        reached.append(cur)
        cur -= stages.count(i)
    fail_rate = [stages.count(i+1) / reached[i] if stages.count(i+1) != 0 else 0 for i in range(N)]
    return [i[0] + 1 for i in sorted(list(enumerate(fail_rate)), key = lambda x: x[1], reverse = True)]