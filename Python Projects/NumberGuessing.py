import random

def random_no(min_value, max_value):
    return random.randint(min_value, max_value)

def main():

    min_value = int(input("Enter the start of the range: "))
    max_value = int(input("Enter the end of the range: "))

    random_number = random_no(min_value, max_value)

    print(f"You have 7 attempts to guess a number between {min_value} and {max_value}.")

    for attempt in range(1, 8):
        guess = int(input(f"Guess {attempt}: "))

        if guess < min_value or guess > max_value:
            print(f"Invalid guess. Please enter a number between {min_value} and {max_value}.")
            continue

        if guess == random_number:
            print("Correct guess!")
            break

        if attempt == 7:
            print(f"Sorry, you ran out of guesses. The number was: {random_number}")
            break

        if guess < random_number:
            print("Try again! You guessed too low.")
        else:
            print("Try again! You guessed too high.")

    restart = input("Do you want to play the game again? (Yes / No): ")
    if restart.lower() == "yes":
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
