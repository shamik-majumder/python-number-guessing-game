# Import Python's built-in 'random' module to handle random number generation
import random

# Print welcome banners and instructions for the player
print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 1 and 100, are you ready? Let's start!")

# Generate a random secret integer between 1 and 100 (inclusive)
choice = random.randint(1, 100)

# Initialize tracking variables:
# - 'user' starts at -1 so the while loop condition (user != choice) evaluates to True initially.
# - 'guesses' keeps a running count of how many attempts the player makes.
user = -1
guesses = 0

# Game Loop: 
# Runs continuously until the user's guess matches the secret random number.
while user != choice:
    # Prompt the user for an integer input and convert it from a string to an int
    user = int(input("Please enter a number Between 1 and 100: "))
    
    # Increment the total guess counter with each new attempt
    guesses += 1

    # --- Conditional Guard Clauses & Feedback ---
    
    # 1. Validation Check: Ensure the user's input falls within the valid game range
    if user < 1 or user > 100:
        print("Invalid choice! Please enter a number between 1 and 100.")
        
    # 2. Too High Check: If the guess is above the secret number, prompt for a lower value
    elif user > choice:
        print("Lower number please.")
        
    # 3. Too Low Check: If the guess is below the secret number, prompt for a higher value
    elif user < choice:
        print("Higher number please.")  
        
    # 4. Correct Guess: The loop condition (user != choice) will break on the next check
    else:
        print(f"Congratulations! You guessed the correct number {choice} in {guesses} guesses.")