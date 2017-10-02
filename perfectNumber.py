#Charlie Goodrich
#10/02/17
#perfectNumber.py - tells you if you have a perfect number

number = int(input("Enter a number: "))

i = 1
total = 0

while i < number:
    if number%i == 0:
        div = number/i
        total += i
    i += 1
if total == number:
    print(number, "is perfect")
else:
    print(number, "is not perfect")