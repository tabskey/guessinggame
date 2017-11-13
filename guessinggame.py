#guessing game

# imports on header for standard since elder times
from random import randrange
import time

# using dictionaries for storing dialogs and messages in a text game
# really nice approach for easy modification
# if it gets big you can have a single dialogs.py and import as var instead :)
dialogs = {
'AskName': "What's your name, darling? ",
'Welcome': ", welcome to the Guessing Game!",
'Goal': "\nYour goal is hit the secret number! ",
'WriteNumber': "Write a number from 1 to 10.",
'SecretIs': "\nThe secret number is ",
'Wrong': "Wrong!Try again!",
'End': "Congrats!"
}

print(dialogs['AskName'])
name = input()

print("\nHello " + name.title() + dialogs['Welcome'])
print(dialogs['Goal'])
print(dialogs['WriteNumber'])
guess = int(input())
secret = randrange(1, 10)

while secret != guess:
	if guess > secret:
		print(dialogs['SecretIs'] + "smaller!")
		print(dialogs['Wrong'])
	elif guess < secret:
		print(dialogs['SecretIs'] + "bigger!")
		print(dialogs['Wrong'])
	guess = int(input())
else:
	print(dialogs['End'])
	time.sleep(2)
