# Find all occurrences of “USA” in a given string ignoring the case
# Solution: https://github.com/JhonesBR

def countUSA(s):
    count = s.lower().count("usa")
    print(f"The USA count is: {count}")


countUSA("Welcome to USA. usa awesome, isn't it?")