# Given a string of words, you need to find the highest 
# scoring word.

# Each letter of a word scores points according to its
# position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that
# appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

import string 

def high(x):
    highest_score = 0
    highest_word = ""
    sentence = x.split()
    for word in sentence:
        score = 0
        for letter in  word:
            score += int((string.ascii_lowercase.index(letter.lower())) + 1)
        if score > highest_score:
            highest_score = score
            highest_word = word
    return highest_word


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))


def high2(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))