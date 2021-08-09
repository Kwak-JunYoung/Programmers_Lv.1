def solution(n, arr1, arr2):
    bin_arr1 = []
    bin_arr2 = []
    answer = []
    for i in range(n):
        bin_string1 = bin(arr1[i])
        if len(bin_string1) < n + 2:
            bin_arr1.append('0' * (n + 2 - len(bin_string1)) + bin_string1[2:])
        else:
            bin_arr1.append(bin_string1[2:])
            
        bin_string2 = bin(arr2[i])
        if len(bin_string2) < n + 2:
            bin_arr2.append('0' * (n + 2 - len(bin_string2)) + bin_string2[2:])
        else:
            bin_arr2.append(bin_string2[2:])

    for i in range(n):
        line = ''
        for j in range(n):
            if bin_arr1[i][j] == '1' or bin_arr2[i][j] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    
    return answer