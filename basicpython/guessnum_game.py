import random

def guess_num():
    guess_num = random.randrange(100)
    chance = 7
    guess_counter = 0

    while guess_counter < chance:
        guess_counter += 1
        my_guess = int(input("enter your guess: "))

        if my_guess==guess_num:
            print("you won")
            break
        elif guess_counter >=chance and my_guess!=guess_num:
            print("try next time")
        elif my_guess < guess_num:
            print("less than guess number")
        elif my_guess > guess_num:
            print("greater than guess number")


guess_num()





