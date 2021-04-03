# Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
# Solution: https://github.com/JhonesBR

def func(s):
    numbers = []
    for word in s.split():
        if word.isdigit():
            numbers.append(float(word))
    return sum(numbers), sum(numbers)/len(numbers)


s = "English = 78 Science = 83 Math = 68 History = 65"
soma, average = func(s)
print(f"Sum: {soma}\nAvarege: {average}")