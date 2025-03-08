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
list_items = [rock , paper , scissors]
user_choice = int(input("Please enter 0 for Rock 1 for Paper and 2 for scissors: "))
random_index = random.randint(0,2)

print(f"Your Choice : {list_items[user_choice]}")
print(f"Computer Choice: {list_items[random_index]}")

if random_index == user_choice:
    print("Nobody won!")
elif user_choice == 0 and random_index == 1:
    print("You lose!")
elif user_choice == 0 and random_index == 2:
    print("You won!")
elif user_choice == 1 and random_index== 0:
    print("You won!")
elif user_choice == 1 and random_index == 2:
    print("You lose!")
elif user_choice == 2 and random_index == 0:
    print("You lose!")
elif user_choice == 2 and random_index == 1:
    print("You won!")
