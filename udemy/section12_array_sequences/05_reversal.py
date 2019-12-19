def rev_word(s):
    words = []
    length = len(s)

    i = 0

    while i < length:
        if s[i] != ' ':
            word_start = i
            while i < length and s[i] != ' ':
                i += 1

            words.insert(0, s[word_start:i])
        i += 1
    
    return ' '.join(words)

print(rev_word('   Hello John    how are you     '))