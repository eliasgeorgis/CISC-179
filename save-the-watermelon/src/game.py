import random

def select_word():
    """Selects and returns a random word from the secret words list."""
    words = ["python", "watermelon", "code", "program", "banana", "computer"]
    return random.choice(words)


def display_word(secret_word, guessed_letters):
    """makes a display string showing guessed letters and underscores for hidden letters."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display


def validate_guess(guess, guessed_letters):
    """ checks if guess is one letter in the alphabet and has not been guessed already"""
    if len(guess) != 1:
        print("Please enter exactly one letter.")
        return False

    if not guess.isalpha():
        print("Invalid input. Please enter an alphabetic letter.")
        return False

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        return False

    return True


def play_game():
    """runs single round of save the watermelon"""
    secret_word = select_word()
    guessed_letters = []
    slices = 6

    print("Welcome to Save the Watermelon")
    print("Guess the secret word one letter at a time before you run out of slices")

    while True:
        """makes a loop that keeps asking for input until the user wins game or loses"""
        print("")
        print(f"Word: {display_word(secret_word, guessed_letters)}")
        print(f"Remaining slices: {slices}")
        print(f"Guessed letters: {guessed_letters}")

        guess = input("Enter a letter: ").lower()

        """Skip to the next turn if the guess is invalid"""
        if not validate_guess(guess, guessed_letters):
            continue
        """adds guess to tracking list and removes slice if its wrong """
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"--> Good guess! '{guess}' is in the word.")
        else:
            slices -= 1
            print(f"--> Sorry, '{guess}' is not in the word. You lost a slice!")

        """checks if all letters are revealed and returns boolean"""
        all_revealed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_revealed = False
                break
        """tells player if they lost or won by checking slices or if all letters are revealed"""
        if all_revealed:
            print("")
            print(f"Congratulations! You saved the watermelon! The word was: {secret_word}")
            break

        if slices <= 0:
            print("")
            print(f" Game Over! You ran out of slices. The word was: {secret_word}")
            break

"""main loop that keeps repeating game if the user says yes"""
def main():
    while True:
        play_game()
        replay = input("\nWould you like to play again? (yes/no): ").lower()
        if replay == "yes":
            print("Starting a new game!")
        else:
            print("Thanks for playing Save the Watermelon! Goodbye!")
            break

main()
