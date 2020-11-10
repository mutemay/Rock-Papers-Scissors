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
game_images = [rock, paper, scissors]

rps = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors \n")
choice = int(rps)
print(game_images[choice])
print("Computer chose:")
computer_choice = random.randint(0,2)
print(game_images[computer_choice])
if choice >= 3 or choice < 0:
  print("You typed an invalid number, you lose.")
elif choice == computer_choice:
  print("It's a draw.")
elif choice == 0 and computer_choice == 2:
  print("You win.")
elif computer_choice == 0 and choice == 2:
  print("You lose")
elif computer_choice > choice:
  print("You lose.")
elif choice > computer_choice:
  print("You win.")
else:
  print("You typed an invalid number, you lose.")