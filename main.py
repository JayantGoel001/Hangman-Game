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
