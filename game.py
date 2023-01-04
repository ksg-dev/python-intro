import random

# prompt user for level n - must be positive

def main():
    level = get_level()
    random = random_integer(level)
    guess = get_guess()
    if random < guess:
        print("Too large!")
    elif random > guess:
        print("Too small!")
    elif random == guess:
        print("Just right!")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            continue
    return(n)

def random_integer(n):
    lev = random.randint(1, n)
    return lev

def get_guess():
    while True:
        try:
            g = int(input("Guess: "))
            if g > 0:
                break
        except ValueError:
            continue
    return(g)

main()
