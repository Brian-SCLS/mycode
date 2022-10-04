#!/usr/bin/env python3

# standard library imports
import random

def main():


    num_picked = random.randrange(1, 50)

    #print(num_picked)

    guess_num = 0

    print("\nNumber Guessing Game")
    print("\nYou have 10 guesses to determine what number between 1 and 50 was chossen. Good luck!")

    while(guess_num < 10):
        user_guess = input("\nWhat is your guess: ")
        user_guess_int = int(user_guess)
        guess_num += 1

        if guess_num == 5:
            print("You only have 5 guesses left")
        elif guess_num == 9:
            print("Oh no!  You only have one guess left.")
        elif guess_num == 10:
            print("\nGame Over! You're not very good at guessing are you?")
            break

        if user_guess_int < num_picked:
            print("Your guess is too low.")
        elif user_guess_int > num_picked:
            print("Your guess is too high.")
        elif user_guess_int == num_picked:
            print("Hooray!  You guessed the number.")
            break

if __name__ == "__main__":
    main()

