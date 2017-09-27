#Charlie Goodrich
#09/27/17
#fives.py - prints out the number of multiples of 5 in a number

number = int(input("Enter a number: "))

amountLeft = number//5
i = 1
while i <= amountLeft:
    print(i*5)
    i += 1
