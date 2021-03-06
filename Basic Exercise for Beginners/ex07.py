# Return the count of sub-string “Emma” appears in the given string
# Solution: https://github.com/JhonesBR

def countEmma(s):
    count = s.count("Emma")
    print(f"Emma appeared {count} times")


s = input()
countEmma(s)