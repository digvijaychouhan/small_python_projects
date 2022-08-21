import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def get_secret_num():
    numbers = list("1234567890")
    random.shuffle(numbers)
    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret):
    clues = []
    for i in range(NUM_DIGITS):
        if guess[i] == secret[i]:
            clues.append("Fermi ")
        elif guess[i] in secret:
            clues.append("Pico ")
    if len(clues) == 0:
        clues.append("Bagels ")
    clues.sort()
    return ''.join(clues)


def main():
    print("""
    ------------------------------------
        Bagels a deductive logic game
    ------------------------------------
    (Clues to play)
    PICO   - One digit is correct but in the wrong position.
    FERMI  - One digit is correct and in right position.
    BAGELS - No digit is correct.""")

    while True:
        secret_number = get_secret_num()
        print(secret_number)
        print("I am thinking of a {}-digit number, can you try to guess.".format(NUM_DIGITS))
        print("You have {} guesses to make it.".format(MAX_GUESSES))

        num_of_guesses = 1
        while num_of_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}:".format(num_of_guesses))
                guess = input("> ")

            clues = get_clues(guess, secret_number)
            print(clues)
            num_of_guesses += 1

            if guess == secret_number:
                print("You guessed it correct!")
                break
            if num_of_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}".format(secret_number))
        print("Do you want to play again? (type yes or no): ")
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing!")


if __name__ == '__main__':
    main()

# print("File __name__ is set to: {}" .format(__name__))
