# Given the following two sets find the intersection and remove those elements from the first set
# First Set  {65, 42, 78, 83, 23, 57, 29}
# Second Set  {67, 73, 43, 48, 83, 57, 29}
# Solution: https://github.com/JhonesBR


def func(s1, s2):
    intersection = s1.intersection(s2)
    for i in intersection:
        s1.remove(i)
    return intersection, s1


s1 = {65, 42, 78, 83, 23, 57, 29}
s2 = {67, 73, 43, 48, 83, 57, 29}
intersection, s1 = func(s1, s2)
print(f"Intersections: {intersection}\nAfter removing: {s1}")