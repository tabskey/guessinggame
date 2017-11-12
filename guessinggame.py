#guessing game
print("What's is your name, darling? ")
name = input()
print("\nHello " + name.title() + ", welcome to the Guessing Game!")

print("\nYour goal is hit the secret number! ")
from random import randrange
import time
secret = randrange(1, 10)
print("Write a number from 1 to 10.")
guess = int(input())

while secret != guess:
	if guess > secret:
		print("\nThe secret number is smaller!")
		print("Wrong!Try again!")
		guess = int(input())
	elif guess < secret:
		print("\nThe secret number is bigger!")
		print("Wrong!Try again!")
		guess = int(input())
else:
	print("Congrats!")
	time.sleep(2)