import random
weapons = ["rock", "paper", "scissors"]
no_of_rounds = 0
n = int(input("No of rounds: "))

user_point  = 0
computer_point = 0

while no_of_rounds < n:
    computer_choice = random.choice(weapons)
    user_choice = input("\n Your choice: ").strip().lower()

    if (computer_choice == "rock" and user_choice == "scissors") or \
            (computer_choice == "scissors" and user_choice == "paper") or \
            (computer_choice == "paper" and user_choice == "rock"):

        print("Computer wins!!")
        computer_point += 1
    elif computer_choice == user_choice:
        print("It is a tie")
    elif user_choice not in weapons:
        print("Invalid choice! Please choose rock,paper or scissors")
        continue
    else:
        print("User wins!!")
        user_point += 1

    no_of_rounds += 1

print(f"Final Score-- User: {user_point} Computer: {computer_point}")

if computer_point > user_point:
    print("YOU LOST!!")
elif computer_point < user_point:
    print("YOU WON!!")
else:
    print("GAME TIES")








