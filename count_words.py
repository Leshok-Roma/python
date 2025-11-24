def count_words (s):
    if not isinstance(s , str):
        raise TypeError("should be string")
    sentence = s.strip()
    if sentence == '':
        return 0 
    words = sentence.split()
    return len(words)


