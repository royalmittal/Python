# guess the number game

import random

print("Guess the number game")
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Random number between", a, "and", b, ": ")
number = random.randrange(a, b)
list = ["Easy", "Medium", "Hard"]
print("Select the difficulty level: ")
for i in range(len(list)):
    print(i+1, list[i])
level = int(input("Enter the level: "))
if level == 1:
    print("You have 20 chances to guess the number")
    chances = 20
elif level == 2:
    print("You have 10 chances to guess the number")
    chances = 10
elif level == 3:
    print("You have 5 chances to guess the number")
    chances = 5
else:
    print("Invalid level")
    exit()
while chances > 0:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations! You guessed the number correctly")
        break
    elif guess < number:
        print("Your guess is less than the number")
    else:
        print("Your guess is greater than the number")
    chances -= 1
    print("Chances left:", chances)
if chances == 0:
    print("You lost the game")
    print("The number was:", number)

