#Charlie Goodrich
#09/27/17
#gauss.py - prints the sum between two numbers

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
difference = int(input("Enter the desired gap between the numbers: "))

total = 0
for i in range(num1, num2+1, difference):
    total += i
    i += 1
print(total)
