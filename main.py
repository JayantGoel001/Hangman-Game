import random


def getWord():
    words = ["superman", "pokemon", "avengers", "aerobics", "sentimental", "australia", "wakanda", "annabell", "jigsaw",
             "kelvin", "facebook", "amazon", "coordination"]
    random_word = random.choice(words)
    return random_word


name = input('Enter Your Name:\n')
print("Welcome", name)
print("==================================")
print("Try To guess in less than 10 moves\n")

word = getWord()
total_guess = 10
misses = []
valid_letters = 'qwertyuiopasdfghjklzxcvbnm'
guessed_word = ['_'] * len(word)


def printFigure(guess):
    pass


while total_guess >= 0:

    print("Misses : ", end='')
    for i in misses:
        print(i, end=" ")
    print()

    print("Moves Remaining : ", total_guess)

    print("Word : ", end="")
    for i in guessed_word:
        print(i, end=' ')
    print()

    guessed_char = input("Make A Guess: ").lower()
    if guessed_char in valid_letters and guessed_char in word:
        for j in range(0, len(word)):
            if word[j] == guessed_char:
                guessed_word[j] = guessed_char
    else:
        total_guess -= 1
        misses.append(guessed_char)
        printFigure(total_guess)

    print()
    if "_" not in guessed_word:
        print("Congratulations!! You Guessed It Right\nWord was\033[1m", word, "\033[0m")
        break
else:
    print("You Let An Innocent man die.")
