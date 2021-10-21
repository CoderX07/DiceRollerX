# Imports Libraries
import random
from time import time
from art import *

# Creates A Dictionary For All The Values On A Dice
numOfEachDiceRoll = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0
}

# Creates An Array With Dice Options
diceOptions = [1, 2, 3, 4, 5, 6]

# Askes For User Input (Number Of Dice Rolls)
numOfRolls = int(input("How many DICE ROLLS would you like? "))

# Begins Timer
timeBegin = time()

# Chooses Random Number From Array
for i in range(numOfRolls):
  diceRoll = random.choice(diceOptions)
  print(diceRoll)
  numOfEachDiceRoll[diceRoll] += 1
  i += 1

# Returns Results
print("-------------------------------")
print()
print("Here Are The Results!")
print()

for key,value in numOfEachDiceRoll.items():
  print(key, ":", value)

# Returns Percentages
print("-------------------------------")
print()
print("And Here Are The Percentages!")
print()

print(f"1 : {numOfEachDiceRoll[1]/numOfRolls * 100}%")
print(f"2 : {numOfEachDiceRoll[2]/numOfRolls * 100}%")
print(f"3 : {numOfEachDiceRoll[3]/numOfRolls * 100}%")
print(f"4 : {numOfEachDiceRoll[4]/numOfRolls * 100}%")
print(f"5 : {numOfEachDiceRoll[5]/numOfRolls * 100}%")
print(f"6 : {numOfEachDiceRoll[6]/numOfRolls * 100}%")
print("-------------------------------")

# Ends Timer
timeEnd = time()

# Displays Timer/Logo
print(f"\nElapsed Time: {timeEnd-timeBegin}")
print()
print("-------------------------------")
print()
tprint("DiceRollerX")