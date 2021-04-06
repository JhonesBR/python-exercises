# Split a given string on hyphens into several substrings and display each substring
# Solution: https://github.com/JhonesBR

def splitHyphens(s):
    for substring in s.split('-'):
        print(substring)


s = "Emma-is-a-data-scientist"
splitHyphens(s)