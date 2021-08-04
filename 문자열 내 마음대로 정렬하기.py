def solution(strings, n):
    strings = sorted(strings, key= lambda x: x[n])
    char_list = [a[n] for a in strings]
    length = len(char_list)
    
    for c in range(length):
        c_count = char_list.count(char_list[c])
        c_index = char_list.index(char_list[c])
        if c_count >= 2 and c == c_index:
            strings[c_index : c_index + c_count] = sorted(strings[c_index : c_index + c_count])
            
    return strings