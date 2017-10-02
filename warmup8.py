#Charlie Goodrich
#10/02/17
#warmup8.py - finds the sum of all positive integers less than 100,000 divisible by 3, 10, and 17

i = 1
total = 0
while i < 100000:
    if i%3 == 0 and i%10 == 0 and i%17 == 0:
        print(total)
    i += 1
    total += i
    
