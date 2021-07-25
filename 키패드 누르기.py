def solution(numbers, hand):
    answer = ''
    ab_left = ['1', '4', '7']
    ab_right = ['3', '6', '9']
    ab_mid = ['2', '5', '8', '0']
    keypad = []
    keypad.extend(['1', '2', '3'])
    keypad.extend(['4', '5', '6'])
    keypad.extend(['7', '8', '9'])
    keypad.extend(['*', '0', '#'])
    cur_left = keypad.index('*')
    cur_right = keypad.index('#')

    for number in numbers:
        s_num = str(number)
        next_pos = keypad.index(s_num)
        
        if s_num in ab_left:
            answer += 'L'
            cur_left = next_pos

        elif s_num in ab_right:
            answer += 'R'
            cur_right = next_pos

        elif s_num in ab_mid:
            right_distance = distance(cur_right, next_pos)
            left_distance = distance(cur_left, next_pos)

            if right_distance < left_distance:
                answer += 'R'
                cur_right = next_pos

            elif right_distance > left_distance:
                answer += 'L'
                cur_left = next_pos

            elif right_distance == left_distance:
                if hand == 'right':
                    answer += 'R'
                    cur_right = next_pos

                elif hand == 'left':
                    answer += 'L'
                    cur_left = next_pos

    return answer

def distance (a, b):
    return abs(a // 3 - b // 3) + abs(a % 3 - b % 3)