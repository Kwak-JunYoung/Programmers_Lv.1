def solution(s):
    num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for num_word in num_words:
        s = s.replace(num_word, str(num_words.index(num_word)))

    return int(s)