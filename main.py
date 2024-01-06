import random
from hangman import hangman_diagram

words = ["ironman", "hulk","thor","loki"]
word = random.choice(words)

def StartGame(word):
    guess_word = [ "_" for i in word ]
    tries = 0
    print(hangman_diagram[tries])
    print("Guess a word : {}".format(" ".join(guess_word)))

    while True:
        user = input("Guess a Letter [a-z] : ")
        if not user.isalpha():
            print("Please enter [a-z] only.")
            continue
        if user in word:
            indexes = [ i for i in range(len(word)) if word[i] == user ]
            for index in indexes:
                guess_word[index] = user
            print("*" * 50)
            print("Good : {}".format("".join(guess_word)))

            if "".join(guess_word) == word:
                return "Wow! You Correct :)"
        else:
            tries = tries + 1
            print(hangman_diagram[tries])
            if tries == 6:
                return "Game Over!!!"
            print("You Incorrect! : {}".format("".join(guess_word)))

if __name__ == "__main__":
    while True:
        print(StartGame(word))
        play_again = input("Do You Want Play Again [y/n] : ")
        if play_again == "y":
            word = random.choice(words)
            continue
        else:
            break