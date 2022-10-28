import random
print("PUT THE FIRST LETTER IN CAPS")
user_action = input("Enter a choice (Rock, Paper, Scissors): ")
possible_actions = ["Rock", "Paper", "Scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "Rock":
    if computer_action == "scissors":
        print("Rock destroyes Scissors! You win!")
    else:
        print("Paper beats Rock! You lose.")
elif user_action == "Paper":
    if computer_action == "Rock":
        print("Paper shits on Rock! You win!")
    else:
        print("Scissors beats Paper! You lose.")
elif user_action == "Scissors":
    if computer_action == "Paper":
        print("Scissors beats Paper! You win!")
    else:
        print("Rock beats Scissors! You lose.")
