# Swap the following two tuples
# Solution: https://github.com/JhonesBR

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1
print(tuple1, tuple2)
