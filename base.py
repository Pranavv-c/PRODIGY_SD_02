import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Prompt the user for their guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid integer.")
            continue

        attempts += 1

        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    number_guessing_game()
