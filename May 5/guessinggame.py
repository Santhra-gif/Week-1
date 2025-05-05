import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Limit the number of guesses
    guess = None
    
    print("\nWelcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.")
    print(f"You have {max_attempts} attempts.\n")
    
    while attempts < max_attempts and guess != number_to_guess:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"\nCongratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
        
        if attempts == max_attempts:
            print(f"\nGame Over! The correct number was {number_to_guess}.")

# Start the game
play_game()
