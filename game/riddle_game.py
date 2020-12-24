import random


def play():
    print("*******************")
    print("Welcome to my game!")
    print("*******************")
    secret_number = random.randint(1, 100)
    shots = 3
    index = 1
    score = 1000
    print("Choose level of the Game")
    print("(1) Easy, (2) Regular, (3) Hard")
    level = int(input("Level: "))
    if level == 1:
        shots = 5
    elif level == 2:
        shots = 10
    else:
        shots = 20
    while index <= shots:
        print("Shot: {} of {}".format(index, shots))
        guess = input("Choose a number: ")
        player_number = int(guess)
        print("Your Number: ", guess)

        user_is_right = secret_number == player_number
        user_number_is_greater = player_number > secret_number
        user_number_is_less = player_number < secret_number

        if player_number < 1 or player_number > 100:
            print("Please type numbers greater than 1 and less than 100")
            continue

        if user_is_right:
            print("You are right")
            break
        else:
            if user_number_is_greater:
                print("Your number is greater than secret number")
            elif user_number_is_less:
                print("Your number is less than secret number")
            score = score - abs(secret_number - shots)

        index += 1
    print(f"Your score is {score}")
    print("Game over")


if __name__ == "__main__":
    play()
