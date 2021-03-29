# Count all lower case, upper case, digits, and special symbols from a given string
# Solution: https://github.com/JhonesBR

def countCDS(s):
    chars, digits, symbols = 0, 0, 0
    for c in s:
        if c.isdigit():
            digits += 1
        else:
            if c.isalpha():
                chars += 1
            else:
                symbols += 1
    print("Chars =", chars)
    print("Digits =", digits)
    print("Symbols =", symbols)


s = "P@#yn26at^&i5ve"
countCDS(s)