# Program: Number Guessing Game


import random

best_score = None   # To store minimum attempts used

while True:
    print("\n=== NUMBER GUESSING GAME ===")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    secret_number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0

    while attempts_left > 0:
        guess = int(input("\nEnter your guess: "))
        attempts_used += 1
        attempts_left -= 1

        if guess == secret_number:
            print("🎉 Congratulations! You guessed correctly.")
            print("Attempts used:", attempts_used)

            # Update best score
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print("🏆 New Best Score!")

            break

        elif guess > secret_number:
            print("Too high!")

        else:
            print("Too low!")

        # Bonus Hint (within 5)
        if abs(guess - secret_number) <= 5 and guess != secret_number:
            print("🔥 Very close!")

        print("Attempts remaining:", attempts_left)

    else:
        # If loop finishes without break
        print("\n❌ You failed!")
        print("The correct number was:", secret_number)

    # Show best score if exists
    if best_score is not None:
        print("Best Score so far:", best_score)

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 😊")
        break