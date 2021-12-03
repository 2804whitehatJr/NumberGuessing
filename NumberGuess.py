import random
print("NUMBER GUESSING GAME")
guess= int(input("ENTER Your guess between 1 to 9"))
number=random.randint(1,9)
if (guess==number):
    print("Congragulations You won")

elif(guess>number):
    print("YOU ARE TOO HIIGH THEN THE GUESS")
    print("The actual guess was: " )
    print(number)

else:
    print("YOU ARE TOO LESS THEN THE GUESS")
    print("The actual guess was: " )
    print(number)





