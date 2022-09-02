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



choice = int(input("What do you pick? 1 for Rock, 2 for Paper, 3 for Scissors: "))
computer = random.randint(1, 3)

print("You picked:\n")
# Your choice
if choice == 1:
    print(rock)
elif choice == 2:
    print(paper)
elif choice == 3:
    print(scissors)

# Computers choice
print("Your opponent picked:\n")
if computer == 1:
    print(rock)
elif computer == 2:
    print(paper)
elif computer == 3:
    print(scissors)

# You loose
if choice == 1 and computer == 2:
    print("You loose!")
elif choice == 2 and computer == 3:
    print("You loose!")
elif choice == 3 and computer == 1:
    print("You loose!")

# You win
if choice == 1 and computer == 3:
    print("You win!")
elif choice == 2 and computer == 1:
    print("You win!")
elif choice == 3 and computer == 2:
    print("You win!")

# Tie
if choice == computer:
    print("Tie! Try again!")