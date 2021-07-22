def solution(array, commands):
    return [sorted(array[c[0] - 1 : c[1]])[c[2] - 1] for c in commands]
