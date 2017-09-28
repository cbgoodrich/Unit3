#Charlie Goodrich
#09/28/17
#divisors.py - asks the user to input a number, prints all of its divisors

number = int(input("Enter a number: "))
i = 1
while number%i == 0:
    print(number / i)
    i += 1
