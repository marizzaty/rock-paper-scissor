import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Welcoming user to the game
print ("Welcome to RPS. Let\'s play!")

#Start the game
weapon = [rock, paper, scissors]
p1_weapon = int(input("0 for Rock, 1 for Paper and 2 for Scissors.\nYou chose: "))


#win or lose??
if p1_weapon > 2 or p1_weapon < 0:
  print("Please try again!")
else:
  player1 = weapon[p1_weapon]
  player2 = random.choice(weapon)

  if (player1 == rock) and (player2 == scissors):
    result = "You win!"
  elif (player1 == scissors) and (player2 == paper):
    result = "You win!"
  elif (player1 == paper) and (player2 == rock):
    result = "You win!"
  elif player1 == player2:
    result = "Draw. Play again."

  else:
    result = "You lose"

  print (player1)
  print (f"Computer chose\n{player2}")
  print (result)


