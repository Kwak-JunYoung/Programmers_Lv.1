def solution(sizes):
    first = []
    second = []
    for size in sizes:
        size.sort()
        first.append(size[0])
        second.append(size[1])
    return (max(first) * max(second))