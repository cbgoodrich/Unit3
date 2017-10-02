#Charlie Goodrich
#10/02/17
#computerChangeLoop.py - tells you the change you have

centTotal = int(input("How many cents do you have? "))


quarters = 0
while centTotal >= 25:
    centTotal = centTotal - 25
    quarters += 1
print("Quarters:", quarters)

dimes = 0
while centTotal >= 10:
    centTotal = centTotal - 10
    dimes += 1
print("Dimes:", dimes)

nickels = 0
while centTotal >= 5:
    centTotal = centTotal - 5
    nickels += 1
print("Nickels:", nickels)

pennies = 0
while centTotal >= 1:
    centTotal = centTotal - 1
    pennies += 1
print("Pennies:", pennies)