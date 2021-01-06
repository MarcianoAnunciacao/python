import random


def play():
    print_welcome_message()
    secret_word = load_secret_word()
    right_words = init_right_word(secret_word)
    print(right_words)

    hanged = False
    correct = False
    errors = 0

    while not hanged and not correct:
        print("Playing")
        shot = input("Try a word")
        shot = shot.strip().upper()

        if shot in secret_word:
            generate_correct_shot(right_words, secret_word, shot)
        else:
            errors += 1
            draw_hang(errors)

        hanged = errors == 7
        correct = "_" not in right_words
        print(right_words)

    if correct:
        print_win_message()
    else:
        print_lose_message(secret_word)

    print("Game Over")


def generate_correct_shot(right_words, secret_word, shot):
    index = 0
    for word in secret_word:
        if shot == word:
            right_words[index] = word
        index += 1


def init_right_word(secret_word):
    return ["_" for _ in secret_word]


def load_secret_word(file="fruits.txt"):
    file = open(file, "r")
    fruits = []
    for line in file:
        line = line.strip()
        fruits.append(line)
    file.close()
    number = random.randrange(0, len(fruits))
    secret_word = fruits[number].upper()
    return secret_word


def print_welcome_message():
    print("************************")
    print("Welcome to Hangman Game!")
    print("************************")


def print_win_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_lose_message(secret_word):
    print("Oh, You were hanged!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
