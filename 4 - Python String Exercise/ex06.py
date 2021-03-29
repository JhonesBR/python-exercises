# Given two strings, s1 and s2, create a mixed String using the following rules
# Note: create a third-string made of the first char of s1 then the last char of s2
# Next, the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.
# Solution: https://github.com/JhonesBR

def merge(s1, s2):
    newString = ""
    length  = len(s1) if len(s1) > len(s2) else len(s2) 
    s2 = s2[::-1]
    for i in range(length):
        if(i < len(s1)):
            newString += s1[i]
        if(i < len(s2)):
            newString += s2[i]
    
    return newString

s1 = "Abc"
s2 = "Xyz"
print(merge(s1, s2))