print("*******************")
print("Welcome to my game!")
print("*******************")

secret_number = 42

guess = input("Enter with a number: ")
player_number = int(guess)
print("Your Number: ", guess)

if secret_number == player_number:
    print("You are right")
else:
    print("You are wrong")

print("Game over")
