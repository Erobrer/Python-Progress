import random
# numb = random.randint(1,1000000)
# is_guessed = False
#
# while not(is_guessed):
#     guess = int(input("Guess the number: "))
#     if guess == numb:
#         print("You guessed it!")
#         is_guessed = True
#     elif guess < numb:
#         print("Too low!")
#     else:
#         print("Too high!")
#


def guess(x):
    random_number = random.randint(1,x)
    user_guess = 0
    while user_guess != random_number:
        user_guess = int(input("Guess the number: "))
        if user_guess < random_number:
            print("Too low!")
        elif user_guess > random_number:
            print("Too high!")

    print("You got it!")


guess(100)


