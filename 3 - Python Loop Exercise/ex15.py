# Use a loop to display elements from a given list that are present at even index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Solution: https://github.com/JhonesBR

def evenIndex(L):
    for i in range(len(L)):
        if (i+1)%2 == 0:
            print(L[i], end=" ")


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
evenIndex(my_list)