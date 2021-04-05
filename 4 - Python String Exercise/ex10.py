# 10: Given an input string, count occurrences of all characters within a string
# Solution: https://github.com/JhonesBR

def countLetters(s):
    letters = {}
    for c in s:
        if c not in letters:
            letters[c] = s.count(c)
    return letters


s = "Apple"
print(countLetters(s))