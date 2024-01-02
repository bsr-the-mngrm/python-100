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

#Write your code below this line 👇

import random

choice = int(input("What do you choose? Type 0 for rock, type 1 for paper or type 2 for scissors \n"))
computer_choice = random.randint(0,2)
rps = [rock, paper, scissors]
result = ""


if (choice == 0 and computer_choice == 0) or (choice == 1 and computer_choice == 1) or (choice == 2 and computer_choice == 2):
    result += "No winner!"
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    result +="You win!"
else:
    result += "You lose!"

print(rps[choice])
print("\nComputer chose:\n" + rps[computer_choice])
print("\n" + result)