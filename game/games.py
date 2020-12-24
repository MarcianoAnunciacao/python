import riddle_game
import hangman_game

print("**********************")
print("Choose your game Game!")
print("**********************")

print("(1) Hangman Game, (2) Riddle Game")

game = int(input("Which Game do you want to play?"))

if game == 1:
    print("Starting Hangman Game...")
    hangman_game.play()
elif game == 2:
    print("Starting Riddle Game...")
    riddle_game.play()
