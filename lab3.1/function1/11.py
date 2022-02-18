word_or_phrase = input()
rev_of_word_or_phrase = word_or_phrase[::-1]

def palindrom(s1,s2):
    if s1 == s2:
        return True
    return False
print(palindrom(word_or_phrase, rev_of_word_or_phrase))
