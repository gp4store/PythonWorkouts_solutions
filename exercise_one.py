# For this exercise: 
# - Write a function (guessing_game) that takes no arguments.
# - When run, the function chooses a random integer between 0 and 100 (inclusive).
# - Then ask the user to guess what number has been chosen.
# - Each time the user enters a guess, the program indicates one of the following:
#     – Too high
#     – Too low
#     – Just right
# - If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
# - The program only exits after the user guesses correctly.

import random
def guessing_game():
    num = random.randint(1, 10)
    name = input(str('Whats your name? '))
    
    while True:
        ans = int(input(f'Whats your guess?  '))
        if ans == num:
            print(f'Thats correct {name}, the answer is {ans}')
            break
        if ans < num:
            print(f'umm no really {name}, {ans} is too low')
        else: 
            print(f'Cmon {name}, {ans} is too low')
        
guessing_game()