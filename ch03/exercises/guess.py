import random
import sys

list=(1,2,3,4,5,6,7,8,9,10)
glist=random.choice(list)
glist=int(glist)
loop=(1,2,3)

for(i) in loop:
  guess=input("Guess a number from 1-10...")
  guess=int(guess)
  if guess==glist:
    print("Correct!")
    sys.exit(" ")
  elif guess < glist:
    print("Too low")
  elif guess > glist:
    print("Too high")
