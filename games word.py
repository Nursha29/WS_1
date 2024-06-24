import random

def choose_word():
    words = ["python", "programming", "computer", "algorithm", "variable", "function", "loop", "syntax", "debugging"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def word_guessing_game():
    max_attempts = 7
    play_again = True

    print("Welcome to the Word Guessing Game!")

    while play_again:
        secret_word = choose_word()
        guessed_letters = []
        attempts = 0
        game_over = False

        print("Try to guess the secret word. It contains", len(secret_word), "letters.")

        while not game_over:
            print("\nWord:", display_word(secret_word, guessed_letters))
            print("Guessed letters:", guessed_letters)
            guess = input("Enter a letter or guess the whole word: ").lower()

            if guess == secret_word:
                print("Congratulations! You guessed the word", secret_word, "correctly!")
                game_over = True
            elif len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You've already guessed that letter. Try again.")
                elif guess in secret_word:
                    print("Good guess!")
                    guessed_letters.append(guess)
                    if all(letter in guessed_letters for letter in secret_word):
                        print("Congratulations! You guessed the word", secret_word, "correctly!")
                        game_over = True
                else:
                    print("Oops! That letter is not in the word.")
                    guessed_letters.append(guess)
                    attempts += 1
                    if attempts >= max_attempts:
                        print("Sorry, you've run out of attempts. The word was", secret_word)
                        game_over = True
            else:
                print("Invalid input. Please enter a single letter or the whole word.")

        play_again = input("Do you want to play again? (yes/no): ").lower().startswith('y')

    print("Thanks for playing!")

# Run the game
word_guessing_game()

