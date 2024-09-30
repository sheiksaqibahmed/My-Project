import random
def guessing_game():
    number_guess = random.randint(1, 10)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        user_guess = input("Guess the number: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        attempts += 1

        if user_guess == number_guess:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
        elif user_guess < number_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

def main():
    try_again = ""
    while try_again.lower() == "":
        guessing_game()
        try_again = input("you can play again ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()