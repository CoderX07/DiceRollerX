import random
from time import time
from art import *

numOfEachDiceRoll = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0
}

diceOptions = [1, 2, 3, 4, 5, 6]

numOfRolls = int(input("How many DICE ROLLS would you like? "))

timeBegin = time()

for i in range(numOfRolls):
  diceRoll = random.choice(diceOptions)
  print(diceRoll)
  numOfEachDiceRoll[diceRoll] += 1
  i += 1

print("-------------------------------")
print()
print("Here Are The Results!")
print()

for key,value in numOfEachDiceRoll.items():
  print(key, ":", value)

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

timeEnd = time()


print(f"\nElapsed Time: {timeEnd-timeBegin}")
print()
print("-------------------------------")
print()
tprint("DiceRollerX")