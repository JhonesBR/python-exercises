# Calculate income tax for the given income by adhering to the below rules
# |------------------------------|
# | Taxable Income | Rate (in %) |
# | -----------------------------|
# | First $10,000  | 0           |
# | -----------------------------|
# | Next $10,000   | 10          |
# | -----------------------------|
# | The Remaining  | 20          |
# | -----------------------------|
# Solution: https://github.com/JhonesBR

def tax(income):
    if income <= 10000:
        pay = 0
    elif income <= 20000:
        pay = (income-10000) * 0.1
    else:
        pay = 10000 * 0.1
        pay += (income-20000) * 0.2
    print(f"Total tax to pay is {pay}")

income = int(input())
tax(income)