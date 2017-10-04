#Charlie Goodrich
#10/04/17
#warmup9.py - inputs a word, prints all the vowels in capitals

word_input = input("Enter a word: ")
word = word_input.lower()


for ch in word:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "y":
        print(ch.upper())
    else:
        print(ch)
