#game where the user has to guess a random number and gets 
#"too hot too cold" idicators until they guess it correctly

import random

secret_num = random.randint(1,100)
you_win = False
min = 1
max = 100

print("\nWelcome to the Number Game \nTry and guess my number between 1 and 100")

while you_win == False:
  val = input("Guess: ")

  val=int(val)

  if val == secret_num:
    you_win = True
    print("YOU WIN!")
    break
  
  if val > max or val < min:
    print("Sorry, your guess is out of bounds\nTry guessing a number between 1 and 100")
    continue

  if val > secret_num:
    print("too high, try again")
  
  else:
    print("too low, try again")
