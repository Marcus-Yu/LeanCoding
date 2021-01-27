import random
print("Welcome to my number guessing game")
a = int(input("Which number would you like to go up to?"))
s = (random.randint(0,a))
b = int(input("Please guess a number."))
while b != s:
  if b == s:
    print("Congratulations, You Guessed the Number!")
  elif b > s:
    print("Your number was too high!")
    b = int(input("Please enter another number."))
  else:
    print("Your number was too low!")
    b = int(input("Please enter another number."))
print("Congratulations, you guessed the number!!!")
print("YOU WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")