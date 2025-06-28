import random
choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
while True:
    print("\n---- Rock Paper Scissors Game ----")
    print(f"Your Score: {user_score} | Computer Score: {computer_score}")
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_choice == 'exit':
        print("\nFinal Scores:")
        print(f"Your Score: {user_score} | Computer Score: {computer_score}")
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
        ):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
