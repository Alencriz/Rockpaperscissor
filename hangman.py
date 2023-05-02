import random

word_list = ["apple", "banana", "orange", "pear", "grape"]
word = random.choice(word_list)
num_attempts = 6
guesses = []
def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display
def check_win(word, guesses):
    for letter in word:
        if letter not in guesses:
            return False
    return True
while num_attempts > 0:
    print(display_word(word, guesses))
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("You already guessed that letter!")
    elif guess in word:
        guesses.append(guess)
        print("Correct!")
    else:
        num_attempts -= 1
        print("Incorrect. You have", num_attempts, "attempts remaining.")
    if check_win(word, guesses):
        print("You win! The word was", word)
        break
    elif num_attempts == 0:
        print("You lose. The word was", word)
        break
display_word()