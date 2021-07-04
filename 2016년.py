def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    day_num = [month[i] for i in range(a)]
   
    sum_day = sum(day_num) + b
    
    answer = day_list[sum_day % 7 - 1]
    
    return answer