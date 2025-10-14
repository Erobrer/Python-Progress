import random

choices = ["rock", "paper", "scissors"]
def game():
    user_choice = input("Choose rock, paper or scissors: " choices)
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"You chose {user_choice}, computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")

game()