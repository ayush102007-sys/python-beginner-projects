import random

words= ['python','brazil','mesh','hello','class','doggy','world','mom','school']
lives = 6

secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)

print("".join(guessed_word))

while lives>0 and "_" in guessed_word:

    guessed_letter = input("Guess a letter: ").strip().lower()
    found_letter = False

    for index,letter in enumerate(secret_word):


        if guessed_letter == letter :

            guessed_word[index] = guessed_letter
            print(guessed_word, f"Lives left {lives}")
            found_letter = True

    if not found_letter:
        lives -= 1
        print(f"Wrong guess! '{guessed_letter}' is not the word.")

    else:
        print(f"Good job! Found '{guessed_letter}'.")

    print("".join(guessed_word))
    print(f"Lives left: {lives}")

if "_" not in guessed_word:
    print("\n YOU WON!!!")
    print(f"You guessed the correct word: {secret_word}")

else:
    print("\n GAME OVER!!")
    print(f"The secret word was: {secret_word}")










