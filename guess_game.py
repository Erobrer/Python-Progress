# print("------------------------------------")
# secret_word = "elephant"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses, you lose.")
# else:
#     print("You win.")
# print("------------------------------------")


print("------------------------------------")
import random
import string

word = input("Enter a word: ")
array = list(word)
print("Word as list:", array)

pc_guess = []
i = 0

while i < len(array):
    a = random.choice(string.ascii_letters)
    if array[i] == a:
        pc_guess.append(a)
        print("Correct guess:", pc_guess)
        i += 1
    else:
        print("Wrong guess:", a)

print("------------------------------------")






