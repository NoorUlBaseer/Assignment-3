"""
Write a Python program that lets a user guess a secret number between 1 and 100.
The program should provide hints whether the guessed number is too high or too low,
and it should continue until the correct number is guessed.

Instructions:
1.	The computer selects a random number between a specified range (e.g., 1 to 100).
2.	You start by guessing a number within that range.
3.	The game tells you whether your guess is too high or too low.
4.	You continue guessing numbers based on the feedback until you guess the correct number.
5.	The game displays the number of attempts it took you to guess correctly.
"""

import random

secret=random.randint(1,100)
count=0
guess=0
while guess!=secret:
    guess=int(input("Guess a number in range 1 to 100: "))
    count+=1
    if (guess<secret):
        print("Too low")
    elif (guess>secret):
        print("Too high")
print("You guessed it after", count, "attempts")
