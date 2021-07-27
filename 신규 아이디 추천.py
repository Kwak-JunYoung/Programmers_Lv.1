def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for char in new_id:
        if char not in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            new_id = new_id.replace(char, '')
    
    # 3단계
    before = ''
    dummy = ''
    for char in new_id:
        if (char == '.' and before != '.') or char != '.':
            dummy += char
        before = char
    
    new_id = dummy
    
    # 4단계
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    
    # 5단계
    if len(new_id) == 0:
        new_id += 'a';
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    
    # 7단계
    if len(new_id) <= 2:
        dummy = new_id[-1]
        while len(new_id) <= 2:
            new_id += dummy
    
    return new_id