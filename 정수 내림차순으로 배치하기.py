def solution(n):
    int_list = sorted([int(i) for i in str(n)], reverse = True)
    ans_str = ''
    for comp in int_list:
        ans_str += str(comp)
    return int(ans_str)