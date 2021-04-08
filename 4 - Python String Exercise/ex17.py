# Find words with both alphabets and numbers
# Solution: https://github.com/JhonesBR

def findWords(s):
    for word in s.split():
        if not (word.isalpha() or word.isdigit()):
            print(word)


s = "Emma25 is Data scientist50 and AI Expert"
findWords(s)