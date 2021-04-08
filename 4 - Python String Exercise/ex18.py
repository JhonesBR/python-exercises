# Replace each punctuation with # in the following string
# Solution: https://github.com/JhonesBR

from string import punctuation

def replacePunctuation(s):
    for c in punctuation:
        s = s.replace(c, "#")
    return s


s = '/*Jon is @developer & musician!!'
print(replacePunctuation(s))