# Find the sum of the series 2 + 22 + 222 + 2222 + .. n terms
# Solution: https://github.com/JhonesBR

def seq(n):
    s = "2"
    series = 0
    for i in range(n):
        series += int(s)
        s += "2"
    print(series)


seq(5)