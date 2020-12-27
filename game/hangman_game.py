def play():
    print("************************")
    print("Welcome to Hangman Game!")
    print("************************")

    secret_word = "Banana".upper()
    right_words = ["_" for word in secret_word]
    hanged = False
    correct = False
    errors = 0

    print(right_words)

    while not hanged and not correct:
        print("Playing")
        shot = input("Try a word")
        shot = shot.strip().upper()

        if shot in secret_word:
            index = 0
            for word in secret_word:
                if shot == word:
                    right_words[index] = word
                index += 1
        else:
            errors += 1

        hanged = errors == 6
        correct = "_" not in right_words
        print(right_words)
    if correct:
        print("You Win!")
    else:
        print("You Lose!")

    print("Game Over")


if __name__ == "__main__":
    play()
