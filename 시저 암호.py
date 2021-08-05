def solution(s, n):
    answer = ''
    for char in s:
        if str(char).isupper():
            answer += str(chr((ord(char) + n  - 65) % 26 + 65))
        elif str(char).islower():
            answer += str(chr((ord(char) + n  - 97) % 26 + 97))
        elif str(char) == ' ':
            answer += ' '
    return answer