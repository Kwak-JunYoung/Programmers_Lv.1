def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("dummy")
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]