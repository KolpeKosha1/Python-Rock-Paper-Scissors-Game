import random


# Function to get user's choice
def get_user_choice():
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter 1, 2, or 3: ")
    return choice


# Function to get computer's choice
def get_computer_choice():
    return str(random.randint(1, 3))
    # here 'a' is start point and 'b' is end point


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == "1" and computer_choice == "3")
            or (user_choice == "2" and computer_choice == "1")
            or (user_choice == "3" and computer_choice == "2")
    ):
        return "You win!"
    else:
        return "Computer wins!"


# Main game loop
while True:
    user_choice = get_user_choice()
    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
