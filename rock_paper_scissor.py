import random

while True:
    user_action = input("Enter a choice (rock, paper, scissor):")
    possible_action = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_action)
    print(f"\n You chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("rock smashes scissors! You win!")
        else:
            print("paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper cover rock! you win.")
        else:
            print("scissor cuts paper you lose.")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("scissor cuts paper! you win!")
        else:
            print("rock smashes paper! you lose!")
    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
        break
