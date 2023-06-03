import random

def play_game():
    # Getting player name and range
    player_name = input("Enter your name: ")
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))

    # Generating random number
    secret_number = random.randint(lower_limit, upper_limit)

    # Initializing variables
    total_points = 100
    round_count = 1

    print(f"\nWelcome, {player_name}! Let's start the game.")

    while True:
        # Prompting user for a guess
        print(f"\nRound {round_count}:")
        guess = int(input("Guess a number: "))

        # Checking the guess
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        # Deducting points for a wrong guess
        total_points -= 5

        # Checking if the user has run out of points
        if total_points <= 0:
            print("\nGame Over! You have run out of points.")
            print(f"The secret number was: {secret_number}")
            break

        # Displaying remaining points
        print(f"Remaining points: {total_points}")

        round_count += 1




play_game()
