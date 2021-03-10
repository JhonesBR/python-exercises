# Format the following data using a string.format() method
# Given:
#   totalMoney = 1000
#   quantity = 3
#   price = 450
# Expected Output:
#   I have 1000 dollars so I can buy 3 football for 450.00 dollars.
# Solution: https://github.com/JhonesBR

totalMoney = 1000
quantity = 3
price = 450

print("I have {} so I can buy {} football for {:.2f} dollars.".format(totalMoney, quantity, float(price)))