import random
import os
import time  


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def choose_difficulty():
    clear_screen()
    print("=== 🎯 Guess the Secret Number! ===")
    print("=== Select Difficulty ===")
    print("1. Easy   (1–100, 10 attempts)")
    print("2. Medium (1–500, 7 attempts)")
    print("3. Hard   (1–1000, 5 attempts)")
    print("e. Exit Game")  

    while True:
        choice = input("Choose (1/2/3 or E to exit): ")

        if choice.lower() == "e":     
            return None, None         

        if choice == "1":
            return 100, 10
        elif choice == "2":
            return 500, 7
        elif choice == "3":
            return 1000, 5
        else:
            print("Invalid choice. Try again.")


def suspense_animation(message="Checking your guess"):
    """Simple dot animation for suspense"""
    print(message, end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print() 


def play_game():
    max_number, max_attempts = choose_difficulty()

    if max_number is None:           
        print("\nThanks for playing! 👋")
        exit()

    number = random.randint(1, max_number)
    attempts = 0

    clear_screen()
    print(f"\nI'm thinking of a number between 1 and {max_number}.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        suspense_animation("Checking your guess")  
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"\n✅ Correct! You guessed the number in {attempts} attempts.")
            break
    else:
        suspense_animation("Calculating result") 
        print(f"\n❌ You're out of attempts! The number was {number}.")

    input("\nPress Enter to get menu...")


def main():
    while True:
        clear_screen()
        print("=== 🎯 Guess the Secret Number! ===")
        play_game()


if __name__ == "__main__":
    main()


print("Hello world")


