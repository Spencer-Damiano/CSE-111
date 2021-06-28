import random


def main():
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")
    print()

    prompt = int(input("Please enter an integer between 1 and 100: "))
    answer = random.randint(1, 100)
    #guess = -1
    tries = 0

    while prompt != answer:
        # Get a guess from the user.
        tries += 1
        #guess = int(prompt)

        # Compare the user's guess to the answer.
        if prompt < answer:
            prompt = int(input(f"{prompt} is too low. Please enter another integer: "))
        elif prompt > answer:
            prompt = int(input(f"{prompt} is too high. Please enter another integer: "))

    print()
    print(f"{prompt} is correct!")
    print(f"You used {tries} guesses to guess my number.")


# If this file was executed like this:
# > python number_guess.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.

if __name__ == "__main__":
    main()
